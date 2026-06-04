
-- Query 1: Top 5 Fund Houses by AUM
SELECT fund_house,
       MAX(aum_crore) AS max_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY max_aum DESC
LIMIT 5;

-- Query 2: Average NAV Per Scheme
SELECT amfi_code,
       ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC
LIMIT 10;

-- Query 3: Transactions by State
SELECT state,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Query 4: Total Investment by State
SELECT state,
       ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;

-- Query 5: Funds with Expense Ratio < 1%
SELECT scheme_name,
       expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- Query 6: Number of Funds by Category
SELECT category,
       COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;

-- Query 7: KYC Status Distribution
SELECT kyc_status,
       COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;

-- Query 8: Transaction Type Distribution
SELECT transaction_type,
       COUNT(*) AS count
FROM fact_transactions
GROUP BY transaction_type;

-- Query 9: Gender-wise Investment
SELECT gender,
       ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY gender;

-- Query 10: Top 10 Funds by Average NAV
SELECT amfi_code,
       ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC
LIMIT 10;
