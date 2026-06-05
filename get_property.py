import sqlite3

def get_property(property_id):

    conn = sqlite3.connect("database/propertyai.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM properties WHERE id=?",
        (property_id,)
    )

    property_data = cursor.fetchone()

    conn.close()

    return property_data