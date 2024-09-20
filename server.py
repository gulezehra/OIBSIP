import socket
import threading

# Function to handle communication with a connected client
def handle_connection(client_conn):
    while True:
        try:
            # Receiving data from the client
            received_data = client_conn.recv(1024).decode('utf-8')
            if received_data:
                print(f"Message from Client: {received_data}")
            else:
                # Disconnect scenario
                print("The client has closed the connection.")
                break
        except Exception as error:
            print(f"Error detected: {error}. Terminating session.")
            break

# Function to allow server-side message sending
def send_to_client(client_conn):
    while True:
        outgoing_msg = input("Server to Client: ")
        client_conn.send(outgoing_msg.encode('utf-8'))

# Setting up the server socket
host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_socket.bind(('127.0.0.1', 5555))  # Server binds to localhost and port 5555
host_socket.listen(1)  # Allow only one client connection at a time

print("The server is active and ready to accept connections...")

# Accepting a client connection
client_conn, client_info = host_socket.accept()
print(f"Connection established with client: {client_info}")

# Start a thread to handle client messages
threading.Thread(target=handle_connection, args=(client_conn,)).start()

# The server will continue to send messages on the main thread
send_to_client(client_conn)
