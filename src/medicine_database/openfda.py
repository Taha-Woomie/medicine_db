from typing import Any

import requests

from .models import Medicine
from .repository import save_medicine


OPENFDA_LABEL_URL = "https://api.fda.gov/drug/label.json"


def fetch_label_records(limit: int = 10, skip: int = 0, timeout: int = 10) -> list[dict[str, Any]]:
    response = requests.get(
        OPENFDA_LABEL_URL,
        params={"limit": limit, "skip": skip},
        timeout=timeout,
    )
    response.raise_for_status()

    return response.json().get("results", [])


def ingest_medicines(limit: int = 10, batch_size: int = 100) -> dict[str, int]:
    saved = 0
    skipped = 0
    remaining = limit
    skip = 0

    while remaining > 0:
        current_limit = min(batch_size, remaining)
        records = fetch_label_records(limit=current_limit, skip=skip)

        if not records:
            break

        for record in records:
            medicine = Medicine.from_openfda_record(record)

            if not medicine:
                skipped += 1
                continue

            save_medicine(medicine)
            saved += 1

        remaining -= len(records)
        skip += len(records)

    return {
        "requested": limit,
        "saved": saved,
        "skipped": skipped,
    }
