CREATE TABLE companies(
    company_id TEXT PRIMARY KEY,
    company_name TEXT
);

CREATE TABLE profitandloss(
    company_id TEXT,
    year INTEGER,
    sales REAL,
    expenses REAL,
    operating_profit REAL
);

CREATE TABLE balancesheet(
    company_id TEXT,
    year INTEGER,
    total_assets REAL,
    total_liabilities REAL
);

CREATE TABLE cashflow(
    company_id TEXT,
    year INTEGER,
    operating_activity REAL,
    investing_activity REAL,
    financing_activity REAL
);

CREATE TABLE analysis(
    company_id TEXT,
    year INTEGER,
    remarks TEXT
);

CREATE TABLE documents(
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id TEXT,
    document_name TEXT
);

CREATE TABLE prosandcons(
    company_id TEXT,
    pros TEXT,
    cons TEXT
);

CREATE TABLE sectors(
    sector_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sector_name TEXT
);

CREATE TABLE stock_prices(
    company_id TEXT,
    trade_date TEXT,
    close_price REAL
);

CREATE TABLE financial_ratios(
    company_id TEXT,
    year INTEGER,
    roe REAL,
    roce REAL,
    pe_ratio REAL
);

CREATE TABLE peer_groups(
    company_id TEXT,
    peer_company TEXT
);