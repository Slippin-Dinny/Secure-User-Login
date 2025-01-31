import sqlite3
import bcrypt

# Connect to SQLite db
conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

# Create table if it doesnt exist already
cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
            id INTERGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            PASSWORD VARCHAR(255) NOT NULL
            )
""")

# Function to hash passwords with bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

# User credentials
users = [
    ("user1", hash_password("pass1")),
    ("John Doe", hash_password("JohnDoePassword"))
]

cur.executemany("INSERT INTO userdata (username, password) VALUES (?, ?)", users)

conn.commit()
conn.close()
