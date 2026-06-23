from db import execute_query


class Medicine:
    def __init__(
        self,
        fda_id,
        brand_name,
        generic_name,
        manufacturer_name,
        substance_name
    ):
        self.fda_id = fda_id
        self.brand_name = brand_name
        self.generic_name = generic_name
        self.manufacturer_name = manufacturer_name
        self.substance_name = substance_name

    def insert(self):
        execute_query(
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
            DO NOTHING
            """,
            (
                self.fda_id,
                self.brand_name,
                self.generic_name,
                self.manufacturer_name,
                self.substance_name
            )
        )

    def __str__(self):
        return (
            f"Medicine("
            f"fda_id='{self.fda_id}', "
            f"brand_name='{self.brand_name}', "
            f"generic_name='{self.generic_name}', "
            f"manufacturer_name='{self.manufacturer_name}', "
            f"substance_name='{self.substance_name}')"
        )