
# Mutual Fund Analytics Capstone - Data Dictionary

## 1. dim_fund (01_fund_master.csv)

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company name |
| scheme_name | Text | Mutual fund scheme name |
| category | Text | Fund category (Equity, Debt, Hybrid) |
| sub_category | Text | Fund sub-category |
| plan | Text | Direct or Regular plan |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Expense ratio percentage |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP investment amount |
| min_lumpsum_amount | Integer | Minimum lump sum investment |
| fund_manager | Text | Fund manager name |
| risk_category | Text | Risk level of fund |
| sebi_category_code | Text | SEBI category code |

---

## 2. fact_nav (clean_nav.csv)

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | Integer | Mutual fund scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## 3. fact_transactions (clean_transactions.csv)

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| investor_id | Text | Unique investor identifier |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Mutual fund scheme code |
| transaction_type | Text | SIP, Lumpsum or Redemption |
| amount_inr | Float | Transaction amount in INR |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | T30 or B30 city classification |
| age_group | Text | Investor age group |
| gender | Text | Investor gender |
| annual_income_lakh | Float | Annual income in lakhs |
| payment_mode | Text | Mode of payment |
| kyc_status | Text | KYC verification status |

---

## 4. fact_performance (clean_performance.csv)

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | Integer | Mutual fund scheme code |
| return_1yr | Float | One-year return (%) |
| return_3yr | Float | Three-year return (%) |
| return_5yr | Float | Five-year return (%) |
| sharpe_ratio | Float | Sharpe ratio |
| sortino_ratio | Float | Sortino ratio |
| alpha | Float | Alpha value |
| beta | Float | Beta value |
| max_drawdown | Float | Maximum drawdown |
| std_dev | Float | Standard deviation |

---

## 5. fact_aum (03_aum_by_fund_house.csv)

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| fund_house | Text | Mutual fund company |
| date | Date | Reporting date |
| aum_crore | Float | Assets Under Management (crore INR) |

---

## Database Tables

1. dim_fund
2. fact_nav
3. fact_transactions
4. fact_performance
5. fact_aum

Prepared for Bluestock Mutual Fund Analytics Capstone Project.
