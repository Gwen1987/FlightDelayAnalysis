from dash import Dash, html, dash_table, dcc, Input, Output
import dash_bootstrap_components as dbc


import pandas as pd
import plotly.express as px

import plotly.graph_objects as go

from datetime import datetime, timedelta


full_df = pd.read_csv('sampled_full_dataframe.csv')
full_df = full_df.rename(columns={'Origin': 'DepAirportCode', 'Dest': 'ArrAirportCode'})

flight_time_df = pd.read_csv('flight_times.csv')
airports_df = pd.read_csv('airports.csv')

airports_df = airports_df.rename(columns={'IATA': 'AirportCode'})

airports_df = airports_df[airports_df['Country'] == "United States"]
print(airports_df)

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])



if 'FlightDate' in full_df.columns:
    full_df['FlightDate'] = pd.to_datetime(full_df['FlightDate'])

full_df['WeekNumber'] = full_df['FlightDate'].dt.isocalendar().week

airports_df['DropdownLabel'] = f'{airports_df['City']} ({airports_df['AirportCode']})'

full_df = full_df.merge(airports_df[['AirportCode', 'City', 'Latitude', 'Longitude']], left_on='DepAirportCode', right_on='AirportCode', how='left')
full_df = full_df.rename(columns={'City': 'DepCity', 'Latitude': 'DepLat', 'Longitude': 'DepLon'})

full_df = full_df.merge(airports_df[['AirportCode', 'City', 'Latitude', 'Longitude']], left_on='ArrAirportCode', right_on='AirportCode', how='left')
full_df = full_df.rename(columns={'City': 'ArrCity', 'Latitude': 'ArrLat', 'Longitude': 'ArrLon'})

print(full_df)


def get_week_ranges():
    year_start = datetime(2025, 1, 1)
    week_ranges = {}

    for week in range(1, 53):
        week_start = year_start + timedelta(weeks=week - 1)
        week_end = week_start + timedelta(days=6)
        week_ranges[week] = f'{week_start.strftime('%b %d')} - {week_end.strftime('%b %d')}'


    return week_ranges

week_ranges = get_week_ranges()

app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Flight Analysis Dashboard", className="text-center mb-4"), width=12)
        ]),
        dbc.Row([
            dbc.Col(html.P("Explore flight delays, routes, and airport statistics.", 
                           className="text-center"), width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Label("Select Starting Location:", className="form-label"),
                        dcc.Dropdown(
                            id='start-location-dropdown',
                            options=[{'label': f"{row['City']} ({row['AirportCode']})", 'value': row['AirportCode']} 
                                     for _, row in airports_df.iterrows()],
                            value=None,
                            placeholder="Select starting location",
                            style={'width': '100%'}
                        )
                    ])
                ])
            ], width=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Label("Select Ending Location:", className="form-label"),
                        dcc.Dropdown(
                            id='end-location-dropdown',
                            options=[{'label': f"{row['City']} ({row['AirportCode']})", 'value': row['AirportCode']} 
                                     for _, row in airports_df.iterrows()],
                            value=None,
                            placeholder="Select ending location",
                            style={'width': '100%'}
                        )
                    ])
                ])
            ], width=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Label("Select Week:", className="form-label"),
                        dcc.Dropdown(
                            id='week-dropdown',
                            options=[{'label': f"Week {week}: {label}", 'value': week} for week, label in week_ranges.items()],
                            value=None,
                            placeholder="Select a week",
                            style={'width': '100%'}
                        )
                    ])
                ])
            ], width=4)
        ], className="mb-4"),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='delay-analysis-graph')
                    ])
                ])
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='map-overlay')
                    ])
                ])
            ], width=12)
        ])
    ], fluid=True, style={"maxWidth": "1200px", "margin": "0 auto"})  # Constrain width and center the dashboard
])


# Callbacks
@app.callback(
    Output('delay-analysis-graph', 'figure'),
    [Input('start-location-dropdown', 'value'),
     Input('end-location-dropdown', 'value'),
     Input('week-dropdown', 'value')]
)
def update_delay_analysis(start_location, end_location, selected_week):
    # Filter data based on selections
    filtered_df = full_df.copy()
    if start_location:
        filtered_df = filtered_df[filtered_df['DepAirportCode'] == start_location]
    if end_location:
        filtered_df = filtered_df[filtered_df['ArrAirportCode'] == end_location]
    if selected_week:
        filtered_df = filtered_df[filtered_df['WeekNumber'] == selected_week]

    # Set the title based on whether a week is selected
    if selected_week:
        title = f"Average Departure Delay by Airline (Week {selected_week}: {week_ranges[selected_week]})"
    else:
        title = "Average Departure Delay by Airline (All Weeks)"

    # Delay Analysis Graph
    delay_fig = px.bar(
        filtered_df.groupby('AirlineName')['DepDelayMinutes'].mean().reset_index(),
        x='AirlineName',
        y='DepDelayMinutes',
        title=title,
        labels={'DepDelayMinutes': 'Average Delay (minutes)', 'AirlineName': 'Airline'}
    )

    return delay_fig

@app.callback(
    Output('map-overlay', 'figure'),
    [Input('start-location-dropdown', 'value'),
     Input('end-location-dropdown', 'value')]
)
def update_map_overlay(start_location, end_location):
    # Create a map with markers for the selected locations
    map_fig = go.Figure()

    if start_location:
        start_row = airports_df[airports_df['AirportCode'] == start_location].iloc[0]
        map_fig.add_trace(go.Scattermapbox(
            lat=[start_row['Latitude']],
            lon=[start_row['Longitude']],
            mode='markers',
            marker=go.scattermapbox.Marker(size=14, color='blue'),
            name=f"Starting Location: {start_row['City']} ({start_row['AirportCode']})"
        ))

    if end_location:
        end_row = airports_df[airports_df['AirportCode'] == end_location].iloc[0]
        map_fig.add_trace(go.Scattermapbox(
            lat=[end_row['Latitude']],
            lon=[end_row['Longitude']],
            mode='markers',
            marker=go.scattermapbox.Marker(size=14, color='red'),
            name=f"Ending Location: {end_row['City']} ({end_row['AirportCode']})"
        ))

    # Configure the map layout
    map_fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=39.8283, lon=-98.5795),  # Centered on the US
            zoom=3
        ),
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        legend=dict(title="Legend")
    )

    return map_fig


if __name__ == '__main__':
    app.run(debug=True)