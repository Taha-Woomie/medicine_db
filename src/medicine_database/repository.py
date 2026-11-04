from .db import fetch_all, fetch_one
from .models import Medicine


MEDICINE_FIELDS = """
    id,
    fda_id,
    brand_name,
    generic_name,
    manufacturer_name,
    substance_name
"""


def save_medicine(medicine: Medicine) -> dict:
    return fetch_one(
        """
        INSERT INTO medicines (
            fda_id,
            brand_name,
            generic_name,
            manufacturer_name,
            substance_name
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (fda_id)
        DO UPDATE SET
            brand_name = EXCLUDED.brand_name,
            generic_name = EXCLUDED.generic_name,
            manufacturer_name = EXCLUDED.manufacturer_name,
            substance_name = EXCLUDED.substance_name
        RETURNING
            id,
            fda_id,
            brand_name,
            generic_name,
            manufacturer_name,
            substance_name
        """,
        (
            medicine.fda_id,
            medicine.brand_name,
            medicine.generic_name,
            medicine.manufacturer_name,
            medicine.substance_name,
        ),
    )


def list_medicines(limit: int = 25, offset: int = 0) -> list[dict]:
    return fetch_all(
        f"""
        SELECT {MEDICINE_FIELDS}
        FROM medicines
        ORDER BY id
        LIMIT %s OFFSET %s
        """,
        (limit, offset),
    )


def get_medicine(medicine_id: int) -> dict | None:
    return fetch_one(
        f"""
        SELECT {MEDICINE_FIELDS}
        FROM medicines
        WHERE id = %s
        """,
        (medicine_id,),
    )


def search_medicines(
    brand_name: str | None = None,
    generic_name: str | None = None,
    manufacturer_name: str | None = None,
    limit: int = 25,
    offset: int = 0,
) -> list[dict]:
    filters = []
    params: list[str | int] = []

    if brand_name:
        filters.append("brand_name ILIKE %s")
        params.append(f"%{brand_name}%")

    if generic_name:
        filters.append("generic_name ILIKE %s")
        params.append(f"%{generic_name}%")

    if manufacturer_name:
        filters.append("manufacturer_name ILIKE %s")
        params.append(f"%{manufacturer_name}%")

    where_clause = f"WHERE {' AND '.join(filters)}" if filters else ""
    params.extend([limit, offset])

    return fetch_all(
        f"""
        SELECT {MEDICINE_FIELDS}
        FROM medicines
        {where_clause}
        ORDER BY id
        LIMIT %s OFFSET %s
        """,
        tuple(params),
    )


def list_medicines_by_manufacturer(
    manufacturer_name: str,
    limit: int = 25,
    offset: int = 0,
) -> list[dict]:
    return fetch_all(
        f"""
        SELECT {MEDICINE_FIELDS}
        FROM medicines
        WHERE manufacturer_name ILIKE %s
        ORDER BY brand_name NULLS LAST, generic_name NULLS LAST
        LIMIT %s OFFSET %s
        """,
        (f"%{manufacturer_name}%", limit, offset),
    )
