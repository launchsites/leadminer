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
        place_id TEXT PRIMARY KEY,
        name TEXT,
        address TEXT,
        website TEXT,
        phone TEXT,
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
        return result[0]
    else:
        return None

def save_lead(place, campaign_name):

    campaign_id = get_campaign_id(campaign_name)
    connection = sort_database()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO leads
    (place_id, name, address, phone, website, rating, reviews, campaign_id)
    VALUES (?,?,?,?,?,?,?,?)
    """, (
        place.placeId,
        place.name,
        place.address,
        place.phone,
        place.website,
        place.rating,
        place.reviews,
        campaign_id
    ))

    connection.commit()
    connection.close()

def list_campaign_data(name: str):
    connection = sort_database()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT leads.name, leads.address, leads.rating, leads.reviews
    FROM leads
    JOIN campaigns ON leads.campaign_id = campaigns.id
    WHERE campaigns.name = ?
    """, (name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()