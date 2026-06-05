import sqlite3

def add_property(
    title,
    location,
    price,
    bedrooms,
    property_type,
    description
):

    conn = sqlite3.connect("database/propertyai.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO properties (
        title,
        location,
        price,
        bedrooms,
        property_type,
        description
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        title,
        location,
        price,
        bedrooms,
        property_type,
        description
    ))

    conn.commit()
    conn.close()

    print("Property added successfully")