import socket
import threading

# Function to receive data from the server
def listen_to_server(client_conn):
    while True:
        try:
            incoming_msg = client_conn.recv(1024).decode('utf-8')
            if incoming_msg:
                print(f"Message from Server: {incoming_msg}")
            else:
                # Server has disconnected
                print("Server has ended the session.")
                break
        except Exception as error:
            print(f"Error occurred: {error}. Shutting down.")
            break

# Setting up the client socket to connect to the server
client_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_conn.connect(('127.0.0.1', 5555))  # Connecting to server's IP and port

# Start a thread to listen for incoming messages from the server
threading.Thread(target=listen_to_server, args=(client_conn,)).start()

# Main thread handles sending messages from the client
while True:
    outgoing_msg = input("Client to Server: ")
    client_conn.send(outgoing_msg.encode('utf-8'))
