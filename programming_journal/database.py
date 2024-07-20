import sqlite3


connection = sqlite3.connect('data.db')

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (entry_content TEXT, entry_date TEXT)")

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute("INSERT INTO entries VALUES (?, ?)", (entry_content, entry_date))


def get_user(username):
    cursor = connection.execute(f"SELECT * FROM users WHERE username = '{username}';")
    return cursor

def get_entries():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM entries")
    # cursor = connection.execute("SELECT * FROM entries")
    # return cursor.fetchall()
    return cursor