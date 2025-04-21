
# ✈️ Flight Delay Analysis ✈️

![GitHub contributors](https://img.shields.io/github/contributors/Gwen1987/FlightDelayAnalysis?style=for-the-badge) / [**Gwen Seymour**](https://github.com/Gwen1987) / [**Peter Lin**](https://github.com/bluejays101) / [**Rob R**](https://github.com/constcorrectness)

---

![MongoDB](https://img.shields.io/badge/MongoDB-4.4.6-green?style=flat-square&logo=mongodb)
![Python](https://img.shields.io/badge/Python-3.8.10-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0.1-red?style=flat-square&logo=flask)
![Pandas](https://img.shields.io/badge/Pandas-1.2.4-orange?style=flat-square&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-1.20.3-blue?style=flat-square&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.2-orange?style=flat-square&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11.1-blue?style=flat-square&logo=seaborn)
![Plotly](https://img.shields.io/badge/Plotly-5.1.0-blue?style=flat-square&logo=plotly)
![Dash](https://img.shields.io/badge/DASH-2.17.0-blue?style=flat-square&logo=dash)

## Overview

#### This project provides an interactive, user-friendly web-based dashboard that visualizes and analyzes historical flight delay data from the US (1999-2019). It enables users to explore delay patterns, identify reliable airlines and airports, and make informed travel planning decisions for specific timeframe.

![Interactive Dashboard](resources/video1.gif)

## Key Features
- **Interactive Data Visualization:** Explore flight delay patterns dynamically with interactive charts and maps.
- **Real-Time Filters:** Select specific airlines, airports, and timeframes to personalize insights.
- **Geo-Spatial Visualization:** Visualize flight routes and delays using interactive maps powered by CesiumJS and Leaflet.
- **Comprehensive Data Analysis:** Evaluate airline reliability through composite reliability metrics and detailed statistical breakdowns.

## Tech Stack
- **Python:** Data processing, analytics, and backend development.
- **Flask:** Web backend serving API endpoints.
- **Mongo Atlas:** Data storage and retrieval.
- **Dash and Plotly:** Interactive dashboard components and visualizations.
- **CesiumJS & Leaflet:** Advanced geo-spatial visualization.
- **Bootstrap:** Responsive and modern frontend styling.

---
### 📁 Folder Structure

```text
FlightDelayAnalysis/
├── FlightDashboard/            # Main application directory
│   ├── dashboard.py            # Dash dashboard (Plotly-based)
│   ├── app.py                  # Flask backend with API routes
│   ├── db_test.py              # MongoDB connection test script
├── full_dataframe.csv          # Raw data used for delay analysis
├── filtered_df.csv             # Cleaned and filtered flight dataset
├── airports_df.csv             # Airport reference data
├── main.ipynb                  # EDA and preprocessing notebook
├── database.ipynb              # ETL workflow and database loading
├── README.md                   # Project documentation
├── requirements.txt            # Required Python packages
└── resources/                  # Images and GIFs for documentation
    └── video1.gif              # Demo animation for dashboard
```
---
## Database

### MongoDB Atlas

  <img src="resources\atlas_db.png" alt="Flight Delay Dashboard" width="1000"/>

Database: `flight_db`  
Collection: `flight_coll`

### Guest access:
- **Username:** `guest`
- **Password:** `guest`

### Connection Example

```python
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://guest:guest@flightcluster.nq9yvyo.mongodb.net/?retryWrites=true&w=majority&appName=FlightCluster"
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['flight_db']
coll = db['flight_coll']

for doc in coll.find({'OriginStateName': 'Colorado'}).limit(5):
    print(doc)
```

Check live DB access [here](https://github.com/Gwen1987/FlightDelayAnalysis/blob/main/db_test.py).

## Setup and Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/Gwen1987/FlightDelayAnalysis.git
```

### Step 2: Navigate to Project Directory
```bash
cd FlightDelayAnalysis/FlightDashboard
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
pip install dash bootstrap components
```

### Step 4: Run Flask Application
```bash
python dashboard.py
```

## Ethical Considerations

Data privacy and user anonymity are crucial. All personal identifiers have been stripped from datasets used, and data used is aggregated and anonymized.

## Data Sources
- Flight data from publicly available databases such as the [Bureau of Transportation Statistics (BTS)](https://www.transtats.bts.gov/).
- Flight data from publicly available databases such as [IBM Developer](https://developer.ibm.com/data/airline/).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.