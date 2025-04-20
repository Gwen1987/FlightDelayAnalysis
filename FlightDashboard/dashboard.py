from dash import Dash, html, dash_table, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Load the data
airports_df = pd.read_csv('airports.csv')
flight_times_df = pd.read_csv('flight_times.csv')
full_df = pd.read_csv('sampled_full_dataframe.csv')

# Rename columns for consistency
full_df = full_df.rename(columns={'Origin': 'DepAirportCode', 'Dest': 'ArrAirportCode'})

# Merge latitude and longitude for departure and arrival airports
airports_df = airports_df.rename(columns={'IATA': 'DepAirportCode'})
full_df = full_df.merge(airports_df[['DepAirportCode', 'Latitude', 'Longitude']], 
                        on='DepAirportCode', how='left')
full_df = full_df.rename(columns={'Latitude': 'DepLat', 'Longitude': 'DepLon'})

airports_df = airports_df.rename(columns={'DepAirportCode': 'ArrAirportCode'})
full_df = full_df.merge(airports_df[['ArrAirportCode', 'Latitude', 'Longitude']], 
                        on='ArrAirportCode', how='left')
full_df = full_df.rename(columns={'Latitude': 'ArrLat', 'Longitude': 'ArrLon'})

# Dashboard
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = "Flight Analysis Dashboard"

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Flight Analysis Dashboard", className="text-center text-primary mb-4"), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.P("Explore flight delays, routes, and airport statistics.", 
                       className="text-center text-secondary"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Label("Select Airport:", className="form-label text-dark"),
                    dcc.Dropdown(
                        id='airport-dropdown',
                        options=[{'label': airport, 'value': airport} for airport in airports_df['Name'].unique()],
                        value=None,
                        placeholder="Select an airport",
                        style={'width': '100%'}
                    )
                ])
            ], className="bg-warning text-dark")
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Label("Select Airline:", className="form-label text-dark"),
                    dcc.Dropdown(
                        id='airline-dropdown',
                        options=[{'label': airline, 'value': airline} for airline in full_df['AirlineName'].unique()],
                        value=None,
                        placeholder="Select an airline",
                        style={'width': '100%'}
                    )
                ])
            ], className="bg-warning text-dark")
        ], width=6)
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='delay-graph')
                ])
            ], className="bg-light text-dark")
        ], width=12)
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='route-map')
                ])
            ], className="bg-light text-dark")
        ], width=12)
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H3("Flight Data Table", className="card-title text-dark"),
                    dash_table.DataTable(
                        id='data-table',
                        columns=[{'name': col, 'id': col} for col in full_df.columns],
                        data=full_df.to_dict('records'),
                        page_size=10,
                        style_table={'overflowX': 'auto'},
                        style_cell={'textAlign': 'left', 'backgroundColor': '#f8f9fa', 'color': '#212529'},
                    )
                ])
            ], className="bg-light text-dark")
        ], width=12)
    ])
], fluid=True, style={"maxWidth": "1200px", "margin": "auto", "backgroundColor": "#fdf6e3"})

# Callbacks
@app.callback(
    [Output('delay-graph', 'figure'),
     Output('route-map', 'figure')],
    [Input('airport-dropdown', 'value'),
     Input('airline-dropdown', 'value')]
)
def update_graphs(selected_airport, selected_airline):
    # Filter data based on selections
    filtered_df = full_df.copy()
    if selected_airport:
        filtered_df = filtered_df[(filtered_df['DepAirportCode'] == selected_airport) | 
                                  (filtered_df['ArrAirportCode'] == selected_airport)]
    if selected_airline:
        filtered_df = filtered_df[filtered_df['AirlineName'] == selected_airline]

    # Delay Graph
    delay_fig = px.bar(
        filtered_df.groupby('DepAirportCode')['DepDelayMinutes'].mean().reset_index(),
        x='DepAirportCode',
        y='DepDelayMinutes',
        title='Average Departure Delay by Airport',
        labels={'DepDelayMinutes': 'Average Delay (minutes)', 'DepAirportCode': 'Airport'}
    )

    # Route Map
    route_fig = px.scatter_geo(
        filtered_df,
        lat='DepLat',
        lon='DepLon',
        color='AirlineName',
        hover_name='DepAirportCode',
        title='Flight Routes (Departure Locations)',
        projection='natural earth'
    )

    return delay_fig, route_fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

