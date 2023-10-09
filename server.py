import socket

# Define the server host and port
host = 'localhost'
port = 65432

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

while True:
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")

    # Receive the file name from the client
    file_name = client_socket.recv(1024).decode()
    print(f"Receiving file: {file_name}")

    try:
        # Open the file for writing
        with open(file_name, 'wb') as file:
            while True:
                # Receive data in chunks
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
        print(f"File received successfully: {file_name}")
        client_socket.send("File received successfully".encode())
    except Exception as e:
        print(f"Error receiving file: {str(e)}")
        client_socket.send(f"Error receiving file: {str(e)}".encode())

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()
