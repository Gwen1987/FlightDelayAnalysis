
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

## 🧭Overview

#### This project provides an interactive, user-friendly web-based dashboard that visualizes and analyzes historical flight delay data from the US (1999-2019). It enables users to explore delay patterns, identify reliable airlines and airports, and make informed travel planning decisions for specific timeframe.

![Interactive Dashboard](resources/video1.gif)

## 📑Key Features
- **Interactive Data Visualization:** Explore flight delay patterns dynamically with interactive charts and maps.
- **Real-Time Filters:** Select specific airlines, airports, and timeframes to personalize insights.
- **Geo-Spatial Visualization:** Visualize flight routes and delays using interactive maps powered by CesiumJS and Leaflet.
- **Comprehensive Data Analysis:** Evaluate airline reliability through composite reliability metrics and detailed statistical breakdowns.

## 🛠Tech Stack
- **Python:** Data processing, analytics, and backend development.
- **Flask:** Web backend serving API endpoints.
- **Mongo Atlas:** Data storage and retrieval.
- **Dash and Plotly:** Interactive dashboard components and visualizations.
- **CesiumJS & Leaflet:** Advanced geo-spatial visualization.
- **Bootstrap:** Responsive and modern frontend styling.

---
### 📁Folder Structure

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
## 🗄Database

### MongoDB Atlas

  <img src="resources\atlas_db.png" alt="Flight Delay Dashboard" width="1000"/>

Database: `flight_db`  
Collection: `flight_coll`

### Guest access:
- **Username:** `guest`
- **Password:** `guest`

### 🔌Connection Example

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

## ⚙️Setup and Installation

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

## 🧠 Key Insights
<p align="center">
  <img src="resources/figure1.png" width="300" height="200" style="display:inline" />
  <img src="resources/figure2.png" width="300" height="200" style="display:inline" />
  <img src="resources/figure3.png" width="300" height="200" style="display:inline" />
  <img src="resources/figure4.png" width="300" height="200" style="display:inline" />
  <img src="resources/figure5.png" width="300" height="200" style="display:inline" />
</p>


1. Consistency vs. Coverage (Figure 1 & Figure 5)
Hawaiian Airlines tops our composite reliability index at 78 %, closely followed by Air Wisconsin and Delta. But Hawaiian’s narrow route network means fewer options if your preferred flight is full. Kalitta Air and SkyWest Airlines also score in the low‑to‑mid 70 % range with remarkably flat delay profiles across all 12 months (see Figure 5’s cooler, uniform cells), suggesting highly predictable service even if absolute OTP % trails the majors. 

**Implication for travellers: If schedule consistency is paramount (e.g. retirees with fixed appointments), consider a smaller carrier like Kalitta or Air Wisconsin despite limited frequency—especially for non‑peak dates in December and January, where these regionals maintain near‑100 % OTP.**


2. Hidden Gems Among Small Hubs (Figure 2)
Airports FOE (Forbes Field, NE) and MIB (Miami Executive) show 100 % reliability, but each handles fewer than 50 flights per year—these “perfect” stats are sample‑size artifacts. By contrast, mid‑sized hubs like PIB (Hattiesburg‑Laurel) and EAR (Kearney, NE) each achieve 93–95 % OTP on several thousand flights annually.

**Takeaway: For those willing to drive a bit further, flying out of a secondary airport can offer near‑guaranteed punctuality plus the comfort of lower crowds—ideal for family groups or seniors wanting a stress‑free departure.**

3. Delay Severity Mix (Figure 3)
Even “best” airlines have non‑zero shares of moderate (16–60 min) and severe (> 60 min) delays. For example, Delta’s 72 % on‑time bar still hides a 12 % 16–60 min bucket and 5 % > 60 min, whereas Kalitta Air squeezes both buckets below 6 % combined. Low‑cost carriers like Spirit and Frontier show the largest > 60 min shares (8–10 %), signaling that a “cheap fare” may cost you an occasional day‑ruining holdup.

**Action: If avoiding “big” delays is a priority—even at the expense of a few additional minutes in the < 15 min bucket—lean toward carriers with the smallest red/orange segments, not necessarily the tallest blue bar.**

4. Seasonality & Holiday Windows (Figure 4)
July and August see the worst average delays (15–22 min) across most carriers, likely due to summer thunderstorms and peak traffic. December (month 12) is actually among the better months for OTP on many airlines—Envoy and US Airways even improve by ~ 2 min compared to annual average—suggesting that holiday routing is fairly well‑managed despite heavier load.

**Recommendation: Travellers targeting the Dec 20–22 window may benefit from the unexpectedly strong December performance of regionals like Envoy and major carriers like United, which in our sample dips only ~ 1 min above its yearly mean.**

5. Balancing Volume with Reliability (Figure 5)
The treemap reveals that Southwest, American, United, and Delta dominate flight counts each month (15 k–21 k flights), but their OTP15 (color scale) spans from 75–85 %—solid but not elite. Envoy, Alaska, and PSA each show OTP15 consistently above 88 %, but account for only 4 k–9 k flights monthly.

**Strategy: Travellers seeking both high on‑time odds and rebooking flexibility should favor Delta or United on their best‑performing days (look for the green‑tinted squares in Dec & Jan), while those willing to accept fewer flight options can lock in Alaska or Envoy for almost worry‑free connections.**

### Putting It All Together:

**Primary axis**: Pick carriers with high composite reliability and low > 60 min delay share (e.g., Hawaiian, Kalitta, Envoy).

**Secondary axis**: Cross‑reference with monthly performance to tailor your specific travel window.

**Tertiary axis**: Ensure you depart from an airport with sufficient flight volume (to avoid sold‑out “perfect” hubs).

## 🌐Ethical Considerations

Data privacy and user anonymity are crucial. All personal identifiers have been stripped from datasets used, and data used is aggregated and anonymized.

## 📊Data Sources
- Flight data from publicly available databases such as the [Bureau of Transportation Statistics (BTS)](https://www.transtats.bts.gov/).
- Flight data from publicly available databases such as [IBM Developer](https://developer.ibm.com/data/airline/).

## 📄License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.