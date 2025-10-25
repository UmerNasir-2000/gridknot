-- ============================================================
-- Schema: gridknot
-- Purpose: Stores API keys and logs of API requests.
-- Author: Umer Nasir
-- ============================================================

-- Create the schema if it doesn't already exist
CREATE SCHEMA IF NOT EXISTS gridknot;

-- ============================================================
-- Table: api_keys
-- Purpose: Holds the list of valid API keys that can access the system.
-- ============================================================
CREATE TABLE IF NOT EXISTS gridknot.api_keys (
    api_key VARCHAR(15) PRIMARY KEY  -- Unique identifier for an API client
);

-- ============================================================
-- Table: request_api_log
-- Purpose: Logs each API request made by clients, tracking its status and timestamps.
-- ============================================================
CREATE TABLE IF NOT EXISTS gridknot.request_api_log (
    request_api_log_id INTEGER PRIMARY KEY,  -- Unique identifier for the request log entry
    api_key VARCHAR(15) NOT NULL REFERENCES gridknot.api_keys(api_key),  -- Links request to a valid API key
    status VARCHAR(15) NOT NULL CHECK (status IN ('BLOCKED', 'PROCESSED')),  -- Only allows valid status values
    expires_on TIMESTAMP NOT NULL DEFAULT NOW() + INTERVAL '1 hour',  -- Expiration time for the request log
    created_at TIMESTAMP NOT NULL DEFAULT NOW()  -- Timestamp when the log was created
);


-- ============================================================
-- Seed Data for api_keys
-- ============================================================

INSERT INTO gridknot.api_keys (api_key) VALUES
    ('sk_live_a8XyP2rN9k3Vb1tR5qL0'),
    ('api_prod_Z9mN7qP0xD3vK8sT2fJ4'),
    ('srv_test_L4bT8cR2pM9aQ6xF1dE5'),
    ('key_stage_A7wD2mS9hL4fR8tQ3vC1'),
    ('client_dev_T5kL1xZ9qR3nC8sV7bM2')
ON CONFLICT DO NOTHING;  -- Avoid duplicate inserts if re-run

-- ============================================================
-- Notes:
-- 1. The CHECK constraint ensures data integrity for the 'status' column.
-- 2. 'expires_on' automatically defaults to one hour after creation.
-- 3. To re-run this script on an existing DB, drop tables manually if needed.
-- ============================================================
