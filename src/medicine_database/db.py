from collections.abc import Iterator
from contextlib import contextmanager

import psycopg2
from psycopg2.extras import RealDictCursor

from .config import get_database_settings


@contextmanager
def get_connection() -> Iterator[psycopg2.extensions.connection]:
    settings = get_database_settings()
    conn = psycopg2.connect(
        host=settings.host,
        port=settings.port,
        dbname=settings.name,
        user=settings.user,
        password=settings.password,
    )

    try:
        yield conn
        conn.commit()
    except psycopg2.Error:
        conn.rollback()
        raise
    finally:
        conn.close()


def execute(query: str, params: tuple | None = None) -> None:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)


def fetch_all(query: str, params: tuple | None = None) -> list[dict]:
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            return list(cursor.fetchall())


def fetch_one(query: str, params: tuple | None = None) -> dict | None:
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            row = cursor.fetchone()
            return dict(row) if row else None
