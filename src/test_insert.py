from medicine_database.models import Medicine
from medicine_database.repository import save_medicine


medicine = Medicine(
    fda_id="manual-example-advil",
    brand_name="Advil",
    generic_name="Ibuprofen",
    manufacturer_name="Pfizer",
    substance_name="Ibuprofen",
)

print(save_medicine(medicine))
