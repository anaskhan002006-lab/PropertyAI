import sqlite3

def register_user(username, email, password):

    conn = sqlite3.connect("database/propertyai.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users
    (username, email, password)
    VALUES (?, ?, ?)
    """, (username, email, password))

    conn.commit()
    conn.close()

    print("User registered successfully")