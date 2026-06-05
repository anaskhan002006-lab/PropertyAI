import sqlite3

def get_properties():

    conn = sqlite3.connect("database/propertyai.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM properties")

    properties = cursor.fetchall()

    conn.close()

    return properties