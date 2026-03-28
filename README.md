# Telecom ETL API Project

## Overview
This project is a simple ETL pipeline using Flask and Pandas.

## Technologies
- Python
- Pandas
- Flask

## API Endpoint
GET /api/v1/telecom

## How to run
pip install pandas flask
python app.py

## Author
Paria Taheri Bandari



## API Endpoint

### GET /api/v1/telecom

This API returns telecom customer data after basic transformation.

### Example Request:
http://127.0.0.1:5000/api/v1/telecom

### Example Response:
```json
[
  {
    "customerID": "1234",
    "tenure": 12,
    "MonthlyCharges": 70.5
  }
]


