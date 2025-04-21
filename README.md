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


## Installation

1. Clone the repository:
   ```bash
   git clone https://www.github.com/Gwen1987/FlightDelayAnalysis.git
   ```
2. Navigate to the project directory:
   ```bash
    cd FlightDelayAnalysis/FlightTracker
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MongoDB database and import the flight delay data into the database. You can use the provided `import_data.py` script to import the data. Make sure to update the MongoDB connection string in the script if necessary.

5. Run the Flask application:
    ```bash
    python dashboard.py
    ```