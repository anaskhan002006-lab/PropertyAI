import sqlite3

def get_admin_stats():

    conn = sqlite3.connect("database/propertyai.db")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM properties")
    total_properties = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM favorites")
    total_favorites = cursor.fetchone()[0]

    conn.close()

    return (
        total_properties,
        total_users,
        total_favorites
    )