-- Total Companies
SELECT COUNT(*) FROM companies;

-- Total Profit & Loss Records
SELECT COUNT(*) FROM profitandloss;

-- Total Balance Sheet Records
SELECT COUNT(*) FROM balancesheet;

-- Total Cash Flow Records
SELECT COUNT(*) FROM cashflow;

-- Top 10 Companies
SELECT * FROM companies LIMIT 10;

-- Highest Sales
SELECT company_id, MAX(sales)
FROM profitandloss;

-- Highest Assets
SELECT company_id, MAX(total_assets)
FROM balancesheet;

-- Highest Operating Cash Flow
SELECT company_id, MAX(operating_activity)
FROM cashflow;

-- Distinct Years
SELECT DISTINCT year
FROM profitandloss;

-- Record Count by Table
SELECT 'companies', COUNT(*) FROM companies
UNION ALL
SELECT 'profitandloss', COUNT(*) FROM profitandloss
UNION ALL
SELECT 'balancesheet', COUNT(*) FROM balancesheet
UNION ALL
SELECT 'cashflow', COUNT(*) FROM cashflow;