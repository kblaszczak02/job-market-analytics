# Job Market Analytics — Poland IT Market Intelligence Dashboard

Data engineering + analytics project built on top of JustJoinIT job offers.
The goal of this project is to analyze the Polish IT job market using Python, Power BI, and real-world job posting data.

---

# Features

## Data Collection

Custom Python scraper for:

* 10,000+ IT job offers
* pagination handling
* deduplication
* salary extraction
* CSV + JSON export
* normalized datasets for analytics

Collected fields include:

* job id
* title
* company
* city
* latitude / longitude
* workplace type
* experience level
* salary ranges
* salary units
* B2B / UoP
* gross / net
* technologies / skills
* publication dates
* categories
* languages
* remote info

---

# Tech Stack

## Backend / Scraping

* Python
* requests
* pandas
* JSON / CSV

## Analytics

* Power BI
* DAX
* Power Query

---

# Dashboard Features

## KPI Cards

* Total Jobs
* Median Salary
* Average Salary
* Remote %
* B2B %
* Top City
* Top Technology

---

## Salary Analytics

### Salary by Experience

Compare median salaries for:

* Junior
* Mid
* Senior
* Lead

---

## Technology Analytics

Top technologies by:

* job count
* median salary
* average salary

Examples:

* Python
* AWS
* Java
* React
* SQL

---

## Remote Work Analysis

Compare:

* remote
* hybrid
* office

Against:

* salary
* offer count
* employment type

---

# Key Insights

Examples of business insights generated from the dashboard:

* AWS increases median salary
* Remote roles offer salary premium
* Senior backend roles dominate salary rankings
* Warsaw and Kraków lead in compensation
* Python + Cloud skills strongly correlate with high-paying offers

---

# Example DAX Measures

## Total Jobs

```DAX
Total Jobs = DISTINCTCOUNT(jobs[id])
```

## Median Salary

```DAX
Median Salary =
MEDIANX(
    FILTER(
        jobs,
        NOT ISBLANK(jobs[salary_avg])
    ),
    jobs[salary_avg]
)
```

## Average Salary

```DAX
Avg Salary =
AVERAGEX(
    FILTER(
        jobs,
        NOT ISBLANK(jobs[salary_avg])
    ),
    jobs[salary_avg]
)
```

---

# Data Challenges

The project handles several real-world data issues:

* duplicate offers
* inconsistent salary units
* missing salary ranges
* multiple employment types
* gross/net normalization
* skill parsing
* API pagination limits

---

# Future Improvements

Planned upgrades:

* daily snapshots
* automated ETL pipeline
* PostgreSQL warehouse
* Airflow scheduling
* salary normalization engine
* skill co-occurrence network graphs
* forecasting models
* ML salary prediction
* real-time dashboard refresh

---

# Project Structure

```bash
job-market-analytics/
│
├── scraper.py
├── jobs.json
├── jobs.csv
├── powerbi/
│   └── dashboard.pbix
├── README.md
└── requirements.txt
```

---

# Running the Scraper

```bash
pip install -r requirements.txt
python scraper.py
```

---

# Disclaimer

This project is for educational and analytical purposes only.
All job posting data belongs to their respective owners.

---

# Author

Karol Błaszczak
