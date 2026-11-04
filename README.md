# Medicine Database API

A small backend practice project that imports medicine label data from the
[openFDA Drug Label API](https://open.fda.gov/apis/drug/label/) into PostgreSQL
and exposes it through a FastAPI service.

## What This Project Practices

- Fetching data from a public API
- Cleaning and mapping external JSON into an internal model
- Writing idempotent inserts/upserts into PostgreSQL
- Building read/search endpoints with FastAPI
- Separating backend code into config, database, repository, API, and ingestion layers

## Project Structure

```text
main.py                         FastAPI entry point
src/ingest_openfda.py           Command-line importer for openFDA data
src/medicine_database/api.py    HTTP routes
src/medicine_database/db.py     PostgreSQL connection helpers
src/medicine_database/models.py Medicine domain model
src/medicine_database/openfda.py openFDA client and importer
src/medicine_database/repository.py SQL queries
src/medicine_database/schemas.py API response schemas
sql/db_init.sql                 Database schema
```

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Create the PostgreSQL database and user, then run:

```bash
psql -U medicine_user -d medicines_db -f sql/db_init.sql
```

For local development, copy `.env.example` to `.env` and adjust the values for
your PostgreSQL setup.

## Import Data

```bash
python src/ingest_openfda.py --limit 50
```

The importer is safe to run more than once. Existing rows with the same FDA ID
are updated instead of duplicated.

## Run the API

```bash
uvicorn main:app --reload
```

Open the generated API docs at:

```text
http://127.0.0.1:8000/docs
```

## Example Endpoints

```text
GET /health
GET /medicines
GET /medicines?brand_name=advil
GET /medicines/{medicine_id}
GET /manufacturers/{manufacturer_name}/medicines
```

## Data Source

Data is provided by the U.S. Food and Drug Administration through openFDA.
