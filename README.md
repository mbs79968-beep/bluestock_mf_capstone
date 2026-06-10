
# Mutual Fund Analytics Platform

## Project Overview

The Mutual Fund Analytics Platform is an end-to-end data analytics project designed to analyze mutual fund performance, investor behavior, portfolio risk, and industry trends. The project combines data engineering, exploratory data analysis, financial analytics, and business intelligence techniques using Python, SQLite, and Power BI.

The platform provides insights into:

* Mutual fund performance evaluation
* Risk and return analysis
* Investor demographics and transaction behavior
* SIP growth and market trends
* Portfolio diversification and concentration risk
* Fund recommendation systems

---

## Project Structure

```text
bluestock_mf_capstone/

├── dashboard/
│   ├── page1.png
│   ├── page2.png
│   ├── page3.png
│   ├── page4.png
│   └── README.md
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks_cleaned/
│   ├── CLEANED_01_data_ingestion.ipynb
│   ├── CLEANED_02_data_cleaning.ipynb
│   ├── CLEANED_03_eda.ipynb
│   ├── CLEANED_04_performance_analysis.ipynb
│   └── CLEANED_05_advanced_analytics.ipynb
│
├── reports/
│   ├── Final_Report.pdf
│   └── charts/
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── compute_metrics.py
│   ├── recommender.py
│   └── run_pipeline.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── data_dictionary.md
└── README.md
```

---

## Datasets Used

The project uses the following datasets:

* Fund Master Data
* NAV History Data
* Portfolio Holdings Data
* Investor Transactions Data
* SIP Inflow Data
* Benchmark Index Data

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQLite
* Power BI
* Git & GitHub

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd bluestock_mf_capstone
```

### 2. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

### 3. Open Jupyter Notebook

```bash
jupyter notebook
```

---

## How to Run ETL

Open and execute:

```text
notebooks_cleaned/CLEANED_01_data_ingestion.ipynb
notebooks_cleaned/CLEANED_02_data_cleaning.ipynb
```

These notebooks perform:

* Data ingestion
* Data validation
* Missing value handling
* Data cleaning
* Feature engineering
* Processed dataset generation

---

## How to Run Analytics

Execute notebooks in the following order:

1. CLEANED_01_data_ingestion.ipynb
2. CLEANED_02_data_cleaning.ipynb
3. CLEANED_03_eda.ipynb
4. CLEANED_04_performance_analysis.ipynb
5. CLEANED_05_advanced_analytics.ipynb

---

## Key Analytics Performed

### Performance Analytics

* Daily Returns
* Annualized Returns
* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown

### Risk Analytics

* Value at Risk (VaR)
* Conditional VaR (CVaR)
* Rolling Sharpe Ratio
* Sector Concentration (HHI)

### Investor Analytics

* Cohort Analysis
* SIP Continuity Analysis
* State-wise Transaction Analysis
* Age Group Analysis

### Recommendation System

* Risk-based Mutual Fund Recommendation Engine

---

## Dashboard

To view the dashboard:

1. Open Microsoft Power BI Desktop.
2. Open the dashboard file:

```text
dashboard/Mutual_Fund_Dashboard.pbix
```

Dashboard Pages:

* Industry Overview
* Fund Performance
* Investor Analytics
* SIP & Market Trends

---

## Deliverables

* Final_Report.pdf
* Power BI Dashboard
* Processed Datasets
* Analytical Reports
* Python Scripts
* SQL Database and Queries

---

## Author

**Bhawani Meena**
IIT Delhi
Mutual Fund Analytics Capstone Project
