# IT Job Market Intelligence Platform

## Project Goal

Build an end-to-end data analytics platform that:
- collects IT job market data from JustJoinIT
- processes and validates the data
- stores structured records in SQLite
- exports datasets for analytics
- visualizes insights in Power BI

The project demonstrates:
- Python automation
- ETL pipelines
- data cleaning
- SQL/database usage
- business intelligence
- dashboard design
- data engineering fundamentals

---

# Final Project Structure

```text
job-market-intelligence/
│
├── scraper/
│   ├── __init__.py
│   ├── justjoinit_scraper.py
│   ├── api_client.py
│   └── utils.py
│
├── processing/
│   ├── __init__.py
│   ├── clean_data.py
│   ├── transform.py
│   ├── validate.py
│   └── skill_parser.py
│
├── database/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   └── jobs.db
│
├── exports/
│   ├── jobs.csv
│   └── skills.csv
│
├── dashboard/
│   ├── JobMarketAnalytics.pbix
│   └── screenshots/
│
├── config/
│   ├── settings.py
│   └── constants.py
│
├── logs/
│   └── scraper.log
│
├── tests/
│   ├── test_cleaning.py
│   ├── test_transform.py
│   └── test_validation.py
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

# Step-by-Step File Breakdown

# 1. main.py

## Purpose
Main ETL pipeline entry point.

Responsible for:
1. extracting job data
2. cleaning and validating data
3. transforming records
4. saving to database
5. exporting CSV files

## Example Workflow

```python
from scraper.justjoinit_scraper import fetch_jobs
from processing.clean_data import clean_jobs
from processing.transform import transform_jobs
from processing.validate import validate_jobs
from database.db import save_jobs

jobs = fetch_jobs()
cleaned = clean_jobs(jobs)
validated = validate_jobs(cleaned)
transformed = transform_jobs(validated)

save_jobs(transformed)
```

---

# 2. scraper/api_client.py

## Purpose
Low-level communication with JustJoinIT API.

Responsibilities:
- sending HTTP requests
- handling errors
- parsing JSON responses
- retry handling

## Recommended Libraries

```python
requests
logging
```

## Professional Features

Add:
- timeout handling
- retry logic
- response validation
- logging

---

# 3. scraper/justjoinit_scraper.py

## Purpose
Main scraping logic.

Responsibilities:
- calling API client
- extracting job records
- selecting useful fields
- normalizing raw responses

## Extract Fields

```text
job title
company
location
salary
remote status
experience level
technologies
employment type
posted date
```

## Output

Return:

```python
list[dict]
```

---

# 4. scraper/utils.py

## Purpose
Reusable helper functions.

Examples:
- date formatting
- salary parsing
- text cleanup
- location formatting

## Example

```python
parse_salary()
normalize_city()
clean_text()
```

---

# 5. processing/clean_data.py

## Purpose
Data cleaning layer.

Responsibilities:
- removing duplicates
- handling missing values
- cleaning salary fields
- normalizing text
- fixing invalid values

## Example Problems

```text
Warsaw vs Warszawa
NULL salaries
duplicate offers
```

---

# 6. processing/validate.py

## Purpose
Data quality validation.

Responsibilities:
- validating salary ranges
- checking required columns
- detecting invalid records
- ensuring data consistency

## Example Rules

```text
salary_min <= salary_max
job_title not empty
location exists
```

This file makes the project look much more professional.

---

# 7. processing/transform.py

## Purpose
Transform raw data into analytics-ready format.

Responsibilities:
- splitting salary ranges
- calculating averages
- creating normalized categories
- preparing tables for Power BI

## Example

Transform:

```text
18k–24k PLN
```

Into:

```text
salary_min = 18000
salary_max = 24000
salary_avg = 21000
```

---

# 8. processing/skill_parser.py

## Purpose
Extract technologies from job descriptions.

## Example

Detect:

```text
Python
SQL
AWS
Docker
React
Azure
```

## Output

Separate skills table:

| job_id | skill |
|---|---|
| 1 | Python |
| 1 | SQL |

This enables better Power BI analytics.

---

# 9. database/schema.sql

## Purpose
Database structure.

## Recommended Tables

### jobs

```sql
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY,
    title TEXT,
    company TEXT,
    city TEXT,
    remote_type TEXT,
    salary_min INTEGER,
    salary_max INTEGER,
    seniority TEXT,
    posted_date TEXT
);
```

### skills

```sql
CREATE TABLE skills (
    id INTEGER PRIMARY KEY,
    job_id INTEGER,
    skill TEXT
);
```

---

# 10. database/db.py

## Purpose
Database operations.

Responsibilities:
- opening SQLite connection
- inserting records
- exporting queries
- handling transactions

## Recommended Libraries

```python
sqlite3
pandas
```

---

# 11. config/settings.py

## Purpose
Central project configuration.

## Store Here

```python
API_URL
REQUEST_TIMEOUT
DATABASE_PATH
EXPORT_PATH
LOG_LEVEL
```

This is standard enterprise structure.

---

# 12. config/constants.py

## Purpose
Static reusable values.

## Examples

```python
SUPPORTED_SKILLS
REMOTE_TYPES
SENIORITY_LEVELS
```

---

# 13. logs/scraper.log

## Purpose
Store execution logs.

## Log Examples

```text
INFO - 320 jobs downloaded
WARNING - Missing salary field
ERROR - API timeout
```

Professional touch.

---

# 14. exports/jobs.csv

## Purpose
Analytics-ready export for Power BI.

## Why Important

Power BI works very well with CSV datasets.

---

# 15. exports/skills.csv

## Purpose
Normalized skills dataset.

Used for:
- top technologies
- skill trends
- demand analysis

---

# 16. dashboard/JobMarketAnalytics.pbix

## Purpose
Main Power BI dashboard.

---

# Recommended Dashboard Pages

## Overview

KPIs:
- total jobs
- average salary
- remote percentage
- top city

Charts:
- jobs by city
- jobs over time
- seniority distribution

---

## Technologies

Charts:
- top skills
- cloud technologies
- AI/ML demand
- backend vs frontend

---

## Salary Analytics

Charts:
- salary by technology
- salary by seniority
- salary by city

---

## Remote Work

Charts:
- remote vs hybrid vs onsite
- remote salaries
- top remote cities

---

# 17. tests/

## Purpose
Basic testing.

You do NOT need advanced testing.

Simple tests already make the repo look mature.

## Example

```python
def test_salary_parser():
    assert parse_salary("18k-24k") == (18000, 24000)
```

---

# 18. requirements.txt

## Recommended

```text
requests
pandas
numpy
sqlite-utils
python-dotenv
pytest
```

Optional:

```text
matplotlib
scikit-learn
```

---

# 19. README.md

## Structure

### Sections

```text
1. Project Overview
2. Features
3. Architecture
4. Tech Stack
5. Installation
6. Usage
7. Dashboard Preview
8. Future Improvements
```

---

# Recommended README Features

Add:
- screenshots
- architecture diagram
- ETL flow
- sample analytics
- Power BI previews

This massively improves portfolio quality.

---

# 20. Future Improvements

## Add Later

- PostgreSQL
- Docker
- FastAPI
- Airflow scheduling
- Streamlit frontend
- ML salary prediction
- Power BI auto-refresh

---

# Final CV Description

## Project Description for CV

**IT Job Market Intelligence Platform**
- Developed Python ETL pipeline for scraping and processing IT job market data
- Implemented data cleaning, validation and analytics workflows using pandas and SQLite
- Built Power BI dashboards for salary, technology and remote work analysis
- Designed structured architecture with reusable scraping and transformation modules

