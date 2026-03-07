import sqlite3
from pathlib import Path

database_path = Path.home() / ".leadminer" / "leadminer.db"

def sort_database():
    database_path.parent.mkdir(exist_ok=True)
    connection = sqlite3.connect(database_path)
    return connection


def make_tables():
    connection = sort_database()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS campaigns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        address TEXT,
        rating REAL,
        reviews INTEGER,
        campaign_id INTEGER,
        FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
    )
    """)

    connection.commit()
    connection.close()

def make_campaign(name: str):
    connection = sort_database()
    cursor = connection.cursor()

    cursor.execute(
    "INSERT INTO campaigns (name) VALUES (?)",
        (name,)
    )

    connection.commit()
    connection.close()

def remove_campaign(name: str):
    connection = sort_database()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM campaigns WHERE name = ?", (name,)
    )

    connection.commit()
    connection.close()

def list_campaigns():
    connection = sort_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT name from campaigns"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row[0])

    connection.close()

def get_campaign_id(name: str):
    connection = sort_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id FROM campaigns WHERE name = ?",
        (name,)
    )

    result = cursor.fetchone()
    connection.close()

    if result is not None:
        return result
    else:
        return None