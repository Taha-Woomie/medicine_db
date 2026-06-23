import requests
from Medicine import Medicine
limit = 10

try:
    response = requests.get(
    "https://api.fda.gov/drug/label.json",
    params={"limit": limit},
    timeout=10
    )

    response.raise_for_status()

    data = response.json()
    
    for record in data["results"]:
        openfda = record.get("openfda", {})
        # field not always present
        if not openfda:
            continue

        medicine = Medicine(
            fda_id=record.get("id"),
            brand_name=openfda.get("brand_name", [None])[0],
            generic_name=openfda.get("generic_name", [None])[0],
            manufacturer_name=openfda.get("manufacturer_name", [None])[0],
            substance_name=openfda.get("substance_name", [None])[0]
        )

        medicine.insert()
        print(medicine)
    
    

except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")

