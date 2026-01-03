# ETL GDP Data Pipeline (Python)

## Overview
This project implements an end-to-end ETL (Extract, Transform, Load) pipeline in Python to collect, process, and store GDP data for countries worldwide.

The pipeline extracts GDP data from a public Wikipedia source (archived via Wayback Machine), transforms the values into standardized units (USD billions), and loads the results into both a CSV file and a SQLite database.

This project was built to demonstrate core data engineering fundamentals using real-world data.

---

## Data Source
- International Monetary Fund (IMF) GDP data  
- Source: Wikipedia (archived snapshot)

---

## Tech Stack
- Python  
- Requests & BeautifulSoup (web scraping)
- Pandas (data transformation)
- SQLite (data storage)

---

## Project Architecture

Each ETL stage is implemented as a separate module to ensure clarity, testability, and extensibility.

---

## How to Run
```bash
git clone https://github.com/Riaz-Uddin-Etu/etl-gdp-data-pipeline.git
cd etl-gdp-data-pipeline
pip install -r requirements.txt
python src/etl_pipeline.py
