CREATE TABLE IF NOT EXISTS medicines (
    id SERIAL PRIMARY KEY,
    fda_id TEXT NOT NULL UNIQUE,
    brand_name TEXT,
    generic_name TEXT,
    manufacturer_name TEXT,
    substance_name TEXT
);

CREATE INDEX IF NOT EXISTS idx_medicines_brand_name
ON medicines (brand_name);

CREATE INDEX IF NOT EXISTS idx_medicines_generic_name
ON medicines (generic_name);

CREATE INDEX IF NOT EXISTS idx_medicines_manufacturer_name
ON medicines (manufacturer_name);
