import sqlite3

def get_favorites():

    conn = sqlite3.connect("database/propertyai.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT p.*
    FROM properties p
    JOIN favorites f
    ON p.id = f.property_id
    """)

    favorites = cursor.fetchall()

    conn.close()

    return favorites