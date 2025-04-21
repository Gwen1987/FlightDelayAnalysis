import React, { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import Select from "react-select";
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
  const [data, setData] = useState([]);
  const [airports, setAirports] = useState([]);
  const [startLocation, setStartLocation] = useState(null);
  const [endLocation, setEndLocation] = useState(null);
  const [week, setWeek] = useState(null);
  const [filteredData, setFilteredData] = useState([]);
  const [weekRanges, setWeekRanges] = useState([]);

  // Load data on component mount
  useEffect(() => {
    // Simulate loading CSV data
    const fetchData = async () => {
      const fullData = await fetch("full_dataframe.json").then((res) =>
        res.json()
      );
      const airportData = await fetch("airports.json").then((res) =>
        res.json()
      );

      // Process week ranges
      const yearStart = new Date(2025, 0, 1); // Jan 1, 2025
      const ranges = Array.from({ length: 52 }, (_, i) => {
        const weekStart = new Date(yearStart);
        weekStart.setDate(weekStart.getDate() + i * 7);
        const weekEnd = new Date(weekStart);
        weekEnd.setDate(weekEnd.getDate() + 6);
        return {
          value: i + 1,
          label: `${weekStart.toLocaleDateString("en-US", {
            month: "short",
            day: "numeric",
          })} - ${weekEnd.toLocaleDateString("en-US", {
            month: "short",
            day: "numeric",
          })}`,
        };
      });

      setData(fullData);
      setAirports(airportData);
      setWeekRanges(ranges);
    };

    fetchData();
  }, []);

  // Filter data based on selections
  useEffect(() => {
    let filtered = data;

    if (startLocation) {
      filtered = filtered.filter(
        (row) => row.DepAirportCode === startLocation.value
      );
    }
    if (endLocation) {
      filtered = filtered.filter(
        (row) => row.ArrAirportCode === endLocation.value
      );
    }
    if (week) {
      filtered = filtered.filter((row) => row.WeekNumber === week.value);
    }

    setFilteredData(filtered);
  }, [startLocation, endLocation, week, data]);

  // Generate delay analysis graph
  const generateDelayGraph = () => {
    if (filteredData.length === 0) {
      return <h5>No data available for selected filters</h5>;
    }

    const airlineData = filteredData.reduce((acc, row) => {
      const airline = row.AirlineName;
      if (!acc[airline]) {
        acc[airline] = { totalDelay: 0, count: 0 };
      }
      acc[airline].totalDelay += row.DepDelayMinutes;
      acc[airline].count += 1;
      return acc;
    }, {});

    const airlines = Object.keys(airlineData);
    const avgDelays = airlines.map(
      (airline) => airlineData[airline].totalDelay / airlineData[airline].count
    );
    const flightCounts = airlines.map(
      (airline) => airlineData[airline].count
    );

    return (
      <Plot
        data={[
          {
            x: airlines,
            y: avgDelays,
            type: "bar",
            text: flightCounts.map((count) => `${count} flights`),
            textposition: "outside",
            marker: { color: "orange" },
          },
        ]}
        layout={{
          title: `Average Departure Delay by Airline ${
            week ? `(Week ${week.label})` : "(All Weeks)"
          }`,
          yaxis: { title: "Average Delay (minutes)" },
          xaxis: { title: "Airline" },
        }}
      />
    );
  };

  // Generate map overlay
  const generateMapOverlay = () => {
    if (!startLocation && !endLocation) {
      return <h5>Select a starting and/or ending location to view the map</h5>;
    }

    const mapData = [];
    if (startLocation) {
      const startAirport = airports.find(
        (airport) => airport.AirportCode === startLocation.value
      );
      mapData.push({
        lat: [startAirport.Latitude],
        lon: [startAirport.Longitude],
        mode: "markers",
        marker: { size: 14, color: "blue" },
        name: `Starting Location: ${startAirport.City} (${startAirport.AirportCode})`,
      });
    }
    if (endLocation) {
      const endAirport = airports.find(
        (airport) => airport.AirportCode === endLocation.value
      );
      mapData.push({
        lat: [endAirport.Latitude],
        lon: [endAirport.Longitude],
        mode: "markers",
        marker: { size: 14, color: "red" },
        name: `Ending Location: ${endAirport.City} (${endAirport.AirportCode})`,
      });
    }

    return (
      <Plot
        data={mapData}
        layout={{
          mapbox: {
            style: "open-street-map",
            center: { lat: 39.8283, lon: -98.5795 }, // Centered on the US
            zoom: 3,
          },
          margin: { r: 0, t: 0, l: 0, b: 0 },
        }}
        config={{ mapboxAccessToken: "pk.eyJ1IjoiaG9ycmlibGVwcm9ncmFtIiwiYSI6ImNtOXFjbjJvMjFpZmIybXB4Zjgzb3d0bzQifQ.V1vzPbiEsTbIFpqlOsOIAQ" }}
      />
    );
  };

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Flight Analysis Dashboard</h1>
      <div className="row mb-4">
        <div className="col-md-4">
          <label>Select Starting Location:</label>
          <Select
            options={airports.map((airport) => ({
              label: `${airport.City} (${airport.AirportCode})`,
              value: airport.AirportCode,
            }))}
            onChange={setStartLocation}
            placeholder="Select starting location"
          />
        </div>
        <div className="col-md-4">
          <label>Select Ending Location:</label>
          <Select
            options={airports.map((airport) => ({
              label: `${airport.City} (${airport.AirportCode})`,
              value: airport.AirportCode,
            }))}
            onChange={setEndLocation}
            placeholder="Select ending location"
          />
        </div>
        <div className="col-md-4">
          <label>Select Week:</label>
          <Select
            options={weekRanges}
            onChange={setWeek}
            placeholder="Select a week"
          />
        </div>
      </div>
      <div className="row mb-4">
        <div className="col-12">{generateDelayGraph()}</div>
      </div>
      <div className="row">
        <div className="col-12">{generateMapOverlay()}</div>
      </div>
    </div>
  );
};

export default App;