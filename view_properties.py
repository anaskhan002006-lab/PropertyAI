import sqlite3

def view_properties():

    conn = sqlite3.connect("database/propertyai.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM properties")

    properties = cursor.fetchall()

    conn.close()

    for property in properties:
        print(property)