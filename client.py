# Client Code
import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to server on localhost, port 9999
    client.connect(("localhost", 9999))

    # Recieve username prompt from the server and send user input
    message = client.recv(1024).decode()
    client.send(input(message).strip().encode())

    # Recieve password prompt from the server and send user input
    message = client.recv(1024).decode()
    client.send(input(message).strip().encode())

    #recieve and print login response from the server
    print(client.recv(1024).decode())
    
    client.close()

if __name__ == "__main__":
    run_client()