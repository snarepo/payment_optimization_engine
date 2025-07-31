# Driver Payout Optimization Framework

A backend experimentation and analytics platform to test and evaluate different driver earnings strategies such as flat bonuses and surge-based payouts. This project demonstrates A/B testing infrastructure, SQL-driven analysis, and platform-style backend architecture for behavioral experimentation.

---

## Overview

This platform enables experimentation on driver payout strategies by:

- Assigning drivers into control and treatment groups
- Persistently tracking experiments, assignments, payouts, and churn
- Running SQL and Python-based analyses to measure impact
- Exposing REST APIs for group assignment and metric reporting
- Supporting synthetic data generation for offline testing

---

## Features

- 🔄 **Group Assignment Engine**: Randomized assignment into experiment groups
- 📊 **Metrics API**: Aggregates churn and earnings metrics by group
- 🧪 **Synthetic Dataset Support**: Simulates driver earnings/churn behavior
- 🧱 **SQL-first Design**: Clear schema for experiments, assignments, payouts
- ⚡ **API-ready**: Exposes endpoints for integration with other services
- 📈 **Notebook Visualization**: Summary dashboards using Pandas + Seaborn

---

## Tech Stack

| Layer       | Technology                        |
|------------|------------------------------------|
| Backend     | Python 3.9, FastAPI, Uvicorn       |
| Database    | SQLite (PostgreSQL-compatible)     |
| Analytics   | SQL, Pandas, Seaborn               |
| Tooling     | curl, Jupyter, shell scripts       |

---

## Project Structure

```
earnings-experimentation-platform/
├── backend/ # Core backend logic
│ ├── main.py # FastAPI app and routes
│ ├── database.py # DB connection and setup
│ ├── experiment_logic.py # Assignment logic
│ ├── analysis.py # Metrics computation
│ └── utils.py # Helpers
├── data/
│ ├── synthetic_data_generator.py
│ └── sample_data.csv
├── notebooks/
│ └── analysis.ipynb # Exploratory visuals
├── sql/
│ ├── create_tables.sql
│ └── sample_queries.sql
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Install dependencies

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Create Database
```
sqlite3 ./data/experiment.db < sql/create_tables.sql
sqlite3 ./data/experiment.db < sql/sample_queries.sql
```

### 3. Run the server
```
uvicorn backend.main:app --reload
```

## API Endpoints

| Endpoint         | Method | Description                                  |
|------------------|--------|----------------------------------------------|
| `/assign`        | POST   | Assigns a driver to a group in an experiment |
| `/metrics/{id}`  | GET    | Returns earnings and churn metrics           |


## SQL Query
SELECT group_name, AVG(earnings) AS avg_earnings, AVG(churned) AS churn_rate
FROM assignments
JOIN payouts USING(driver_id)
JOIN drivers USING(driver_id)
WHERE experiment_id = 1
GROUP BY group_name;


## Use Case
Sample Use Case
Create or simulate an experiment with drivers

Assign drivers to control/treatment groups via the API

Simulate payout and churn behavior

Use metrics endpoint or notebook to compare performance


## Outcomes
Simulates realistic A/B experimentation on payout strategies

Enables data-driven evaluation of earnings configurations

Modular and extensible for real-world experimentation pipelines



