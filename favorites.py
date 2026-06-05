import sqlite3

def add_favorite(property_id):

    conn = sqlite3.connect("database/propertyai.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO favorites (property_id) VALUES (?)",
        (property_id,)
    )

    conn.commit()
    conn.close()

    print("Added to favorites")