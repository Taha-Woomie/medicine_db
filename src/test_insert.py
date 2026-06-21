from db import execute_query
from db import execute_query_select

execute_query(
    """
    INSERT INTO medicines
    (brand_name, generic_name, manufacturer_name)
    VALUES (%s, %s, %s)
    """,
    (
        "Advil",
        "Ibuprofen",
        "Pfizer"
    )
)

print(execute_query_select("SELECT * FROM medicines"))