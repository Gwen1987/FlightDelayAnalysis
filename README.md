# FlightDelayAnalysis


![GitHub contributors](https://img.shields.io/github/contributors/Gwen1987/FlightDelayAnalysis?style=for-the-badge)




![MongoDB](https://img.shields.io/badge/MongoDB-4.4.6-green?style=flat-square&logo=mongodb)
![Python](https://img.shields.io/badge/Python-3.8.10-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0.1-red?style=flat-square&logo=flask)
![Pandas](https://img.shields.io/badge/Pandas-1.2.4-orange?style=flat-square&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-1.20.3-blue?style=flat-square&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.2-orange?style=flat-square&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11.1-blue?style=flat-square&logo=seaborn)
![Plotly](https://img.shields.io/badge/Plotly-5.1.0-blue?style=flat-square&logo=plotly)
![DASH](https://img.shields.io/badge/DASH-2.17.0-blue?style=flat-square&logo=dash)

## Example

<img src="resources/video1.gif" />

## Description

This project is a web application that provides an interactive dashboard for analyzing flight delay data. The application allows users to visualize and explore flight delay patterns, trends, and correlations using various data visualization techniques. It utilizes Flask as the backend framework and MongoDB as the database for storing flight delay data.


## Features

- Interactive dashboard for visualizing flight delay data
- Data filtering and selection options



## Technologies Used

- Python
- Flask
- MongoDB
- Pandas
- NumPy
- Matplotlib


## Atlas MongoDB 

![Atlas](resources/atlas_db.png)

Database -> flight_db
Collection -> flight_coll

see [connect.py](https://github.com/Gwen1987/FlightDelayAnalysis/blob/main/connect.py)

_Guest Access_
- username: guest
- password: guest



```python
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://guest:guest@flightcluster.nq9yvyo.mongodb.net/?retryWrites=true&w=majority&appName=FlightCluster"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    db = client['flight_db']
    coll = db['flight_coll']
    print(coll.find({'OriginStateName': 'Colorado'}))
except Exception as e:
    print(e)
```

_run live DB access [demo](https://github.com/Gwen1987/FlightDelayAnalysis/blob/main/db_test.py)_


## Installation

1. Clone the repository:
   ```bash
   git clone https://www.github.com/Gwen1987/FlightDelayAnalysis.git && cd FlightDelayAnalysis
   ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Generate the .csv files needed for the dashboard (run the main.ipynb to generate):
    - dataframes/full_dataframe.csv
    - dataframes/filtered_df.csv
    - dataframes/airports_df.csv
    - dataframes/flight_times.csv

4. Navigate to the dashboard directory (FlightTracker subdirectory):
   ```bash
    cd FlightTracker
    ```

5. Run the DASH application:
    ```bash
    python dashboard.py
    ```

