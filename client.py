import socket

# Define the server host and port
host = 'localhost'
port = 65432

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Specify the file to send
file_name = 'example1.txt'

# Send the file name to the server
client_socket.send(file_name.encode())

try:
    # Open the file for reading
    with open(file_name, 'rb') as file:
        while True:
            # Read data in chunks
            data = file.read(1024)
            if not data:
                break
            # Send data to the server
            client_socket.send(data)
    print("File sent successfully")
except Exception as e:
    print(f"Error sending file: {str(e)}")

# Receive acknowledgment from the server
response = client_socket.recv(1024).decode()
print(response)

# Close the client socket
client_socket.close()
