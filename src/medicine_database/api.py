from fastapi import FastAPI, HTTPException, Query

from .repository import (
    get_medicine,
    list_medicines,
    list_medicines_by_manufacturer,
    search_medicines,
)
from .schemas import MedicineResponse


app = FastAPI(
    title="Medicine Database API",
    description="A small backend service for importing and searching openFDA medicine label data.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/medicines", response_model=list[MedicineResponse])
def read_medicines(
    brand_name: str | None = Query(default=None),
    generic_name: str | None = Query(default=None),
    manufacturer_name: str | None = Query(default=None),
    limit: int = Query(default=25, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
) -> list[dict]:
    has_filters = brand_name or generic_name or manufacturer_name

    if has_filters:
        return search_medicines(
            brand_name=brand_name,
            generic_name=generic_name,
            manufacturer_name=manufacturer_name,
            limit=limit,
            offset=offset,
        )

    return list_medicines(limit=limit, offset=offset)


@app.get("/medicines/{medicine_id}", response_model=MedicineResponse)
def read_medicine(medicine_id: int) -> dict:
    medicine = get_medicine(medicine_id)

    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")

    return medicine


@app.get("/manufacturers/{manufacturer_name}/medicines", response_model=list[MedicineResponse])
def read_medicines_by_manufacturer(
    manufacturer_name: str,
    limit: int = Query(default=25, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
) -> list[dict]:
    return list_medicines_by_manufacturer(
        manufacturer_name=manufacturer_name,
        limit=limit,
        offset=offset,
    )
