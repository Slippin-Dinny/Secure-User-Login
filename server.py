import sqlite3
import socket
import bcrypt
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the server to the localhost on port 9999 but this can be edited to host the server online 
server.bind(("localhost", 9999))

# Begin listening for incoming connections
server.listen()

# Function to handle for when a client connects
def handle_connection(c):
    # Prompt client for username
    c.send("Username: ".encode())
    username = c.recv(1024).decode().strip()

    # Prompt client for password
    c.send("Password: ".encode())
    password = c.recv(1024).decode().strip().encode()

    # Connect to SQLite database
    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

    # Retrieve the stored password hash for the username
    cur.execute("SELECT password FROM userdata WHERE username = ?", (username,))
    result = cur.fetchone()

    # Verify the provided password against the stored hash
    if result and bcrypt.checkpw(password, result[0]):
        c.send("Login successful!".encode())
    else:
        c.send("Login failed!".encode())

    conn.close()
    c.close()

# Loop to continuously accept new client connections and to spawn a new thread for each
while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()