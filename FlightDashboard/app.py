from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load preprocessed DataFrame on startup
flight_df = pd.read_csv("flight_times.csv")



@app.route('/')
def index():
    return render_template('dashboard.html')
    # return render_template('index.html')
    # return render_template('cesium.html')


@app.route('/get_delays')
def get_delays():
    airline = request.args.get('airline')
    if airline and airline != 'ALL':
        filtered = flight_df[flight_df['AirlineName'] == airline]
    else:
        filtered = flight_df
    
    delays_by_airport = filtered.groupby('DepAirportCode').agg(avg_delay=('DepDelayMinutes', 'mean'), count=('DepDelayMinutes', 'count'))

    return jsonify(delays_by_airport.to_dict(orient='records'))


@app.route('/data')
def flight_data():
    airline = request.args.get('airline', '')
    hour = request.args.get('hour', '')

    # Filter
    df = flight_df.copy()

    if airline:
        df = df[df['AirlineName'] == airline]

    if hour:
        try:
            hour_int = int(hour)
            df = df[df['DepTime'].fillna(0).astype(int) // 100 == hour_int // 100]
        except ValueError:
            pass



    df = df.where(pd.notnull(df), None)


    features = []
    for _, row in df.iterrows():
        dep_lat, dep_lon = row['DepLat'], row['DepLon']
        arr_lat, arr_lon = row['ArrLat'], row['ArrLon']

        if pd.notna(dep_lat) and pd.notna(arr_lat):
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [row['DepLon'], row['DepLat']],
                        [row['ArrLon'], row['ArrLat']]
                    ]
                },
                "properties": {
                    "airline": row['AirlineName'],
                    "dep_code": row['DepAirportCode'],
                    "arr_code": row['ArrAirportCode'],
                    "dep_time": row['DepTime'],
                    "arr_time": row['ArrTime'],
                    "dep_delay": row['DepDelayMinutes'],
                    "arr_delay": row['ArrDelayMinutes']
                }
            }
            features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return jsonify(geojson)

@app.route('/delay_data')
def delay_data():
    # Get query parameters
    airline = request.args.get('airline', '')
    airport = request.args.get('airport', '')

    # Filter the DataFrame
    df = flight_df.copy()

    if airline:
        df = df[df['AirlineName'] == airline]

    if airport:
        df = df[(df['DepAirportCode'] == airport) | (df['ArrAirportCode'] == airport)]

    # Group by departure airport and calculate average delay
    delay_summary = df.groupby('DepAirportCode').agg(
        avg_delay=('DepDelayMinutes', 'mean'),
        flight_count=('DepDelayMinutes', 'count')
    ).reset_index()

    # Replace NaN with 0 for JSON compatibility
    delay_summary = delay_summary.fillna(0)

    # Convert to JSON format
    return jsonify({
        "labels": delay_summary['DepAirportCode'].tolist(),
        "delays": delay_summary['avg_delay'].tolist(),
        "flight_counts": delay_summary['flight_count'].tolist()
    })

@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')

if __name__ == '__main__':
    app.run(debug=True)