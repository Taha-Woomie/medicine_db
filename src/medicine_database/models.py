from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Medicine:
    fda_id: str
    brand_name: str | None
    generic_name: str | None
    manufacturer_name: str | None
    substance_name: str | None

    @classmethod
    def from_openfda_record(cls, record: dict[str, Any]) -> "Medicine | None":
        openfda = record.get("openfda") or {}
        fda_id = record.get("id")

        if not fda_id or not openfda:
            return None

        return cls(
            fda_id=fda_id,
            brand_name=_first_value(openfda.get("brand_name")),
            generic_name=_first_value(openfda.get("generic_name")),
            manufacturer_name=_first_value(openfda.get("manufacturer_name")),
            substance_name=_first_value(openfda.get("substance_name")),
        )


def _first_value(value: Any) -> str | None:
    if isinstance(value, list) and value:
        return value[0]

    if isinstance(value, str):
        return value

    return None
