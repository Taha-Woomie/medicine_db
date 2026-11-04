import argparse

import requests

from medicine_database.openfda import ingest_medicines


def main() -> None:
    parser = argparse.ArgumentParser(description="Import medicine label data from openFDA.")
    parser.add_argument("--limit", type=int, default=10, help="Number of openFDA records to request.")
    parser.add_argument("--batch-size", type=int, default=100, help="Records to fetch per API request.")
    args = parser.parse_args()

    try:
        summary = ingest_medicines(limit=args.limit, batch_size=args.batch_size)
    except requests.RequestException as exc:
        print(f"openFDA request failed: {exc}")
        raise SystemExit(1) from exc

    print(
        "Import complete: "
        f"requested={summary['requested']} "
        f"saved={summary['saved']} "
        f"skipped={summary['skipped']}"
    )


if __name__ == "__main__":
    main()
