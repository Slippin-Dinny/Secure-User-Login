# Secure-User-Login
Python script which runs a secure server login interface

# Usage
* Step 1: Run the createDB.py file to create a SQLite database with preset user and passwords, the server relies upon the presence of the database to function.
* Step 2: Run the server.py file, make any nessecary changes to the host or port of the server if you are interested in hosting the server across the network.
* Step 3: Finally, run the client.py file, this will connect to the server and will prompt for a username and password, after entering both the server should alert you on whether you were succesful or not.
