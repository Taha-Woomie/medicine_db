import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class DatabaseSettings:
    host: str
    port: int
    name: str
    user: str
    password: str


def get_database_settings() -> DatabaseSettings:
    return DatabaseSettings(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        name=os.getenv("DB_NAME", "medicines_db"),
        user=os.getenv("DB_USER", "medicine_user"),
        password=os.getenv("DB_PASSWORD", "password"),
    )
