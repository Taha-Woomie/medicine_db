-- initial mockup, can be expanded later
CREATE TABLE medicines (
    id SERIAL PRIMARY KEY,
    fda_id TEXT UNIQUE,
    brand_name TEXT,
    generic_name TEXT,
    manufacturer_name TEXT,
    substance_name TEXT
);

ALTER TABLE medicines
ADD CONSTRAINT unique_medicine
UNIQUE (
    brand_name,
    generic_name,
    manufacturer_name
);