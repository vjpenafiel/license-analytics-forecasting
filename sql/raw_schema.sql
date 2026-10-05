-- Create SQL schema for raw data
CREATE SCHEMA IF NOT EXISTS raw;

-- 1. Table for users
CREATE raw.users (
    user_id VARCHAR(50) PRIMARY KEY,
    job_role VARCHAR(255),
    location VARCHAR(50),
    created_at DATE
);

-- 2. Table for software products   
CREATE raw.software_products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    vendor VARCHAR(255) NOT NULL,
    version VARCHAR(50)
);

-- 3. Table for software features
CREATE raw.software_features (
    feature_id VARCHAR(50) PRIMARY KEY,
    product_id VARCHAR(50) REFERENCES raw.software_products(product_id),
    feature_name VARCHAR(255) NOT NULL,
    feature_category VARCHAR(255),
    version VARCHAR(50)
);

-- 4. Table for license pools
CREATE raw.license_pools (
    license_pool_id VARCHAR(50) PRIMARY KEY,
    product_id VARCHAR(50) REFERENCES raw.software_products(product_id),
    capacity INT NOT NULL,
    valid_from DATE,
    valid_until DATE
)

-- 5. Table for license events
-- NOTE: Omit foreign keys to allow messy data for further data cleaning
CREATE raw.license_events (
    event_id BIGINT PRIMARY KEY,
    event_timestamp TIMESTAMP NOT NULL,
    user_id VARCHAR(50),
    product_id VARCHAR(50),
    feature_id VARCHAR(50),
    license_pool_id VARCHAR(50),
    event_type VARCHAR(50) NOT NULL,
    session_id VARCHAR(255),
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

-- 6. Indexing for query performance
CREATE INDEX idx_raw_events_session ON raw.license_events(session_id);
CREATE INDEX idx_raw_events_ts ON raw.license_events(event_timestamp);
CREATE INDEX idx_raw_events_user ON raw.license_events(user_id);
CREATE INDEX idx_raw_events_feature ON raw.license_events(feature_id);
CREATE INDEX idx_raw_events_product ON raw.license_events(product_id);
CREATE INDEX idx_raw_events_pool ON raw.license_events(license_pool_id);

