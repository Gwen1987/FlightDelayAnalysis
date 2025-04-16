from flask import Flask, render_template, request, jsonify
import pandas as pd
import json

app = Flask(__name__)

# Load preprocessed DataFrame on startup
flight_times_df = pd.read_csv("flight_times.csv")

@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('cesium.html')


@app.route('/data')
def flight_data():
    airline = request.args.get('airline', '')
    hour = request.args.get('hour', '')

    # Filter
    df = flight_times_df.copy()

    if airline:
        df = df[df['AirlineName'] == airline]

    if hour:
        try:
            hour_int = int(hour)
            df = df[df['DepTime'].fillna(0).astype(int) // 100 == hour_int // 100]
        except ValueError:
            pass


    print(df.columns)


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

if __name__ == '__main__':
    app.run(debug=True)