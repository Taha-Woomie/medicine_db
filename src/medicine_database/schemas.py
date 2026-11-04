from pydantic import BaseModel


class MedicineResponse(BaseModel):
    id: int
    fda_id: str
    brand_name: str | None = None
    generic_name: str | None = None
    manufacturer_name: str | None = None
    substance_name: str | None = None
