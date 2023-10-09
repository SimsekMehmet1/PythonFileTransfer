# PythonFileTransfer
This repository contains a simple Python implementation of an echo client and server that can transfer files over a network using sockets.

Server (server.py)
The server listens for incoming connections on a specified host and port. When a client connects, it performs the following steps:

Accepts the client connection.
Receives the name of the file to be transferred from the client.
Opens the file for writing.
Receives data in chunks from the client and writes it to the file.
Sends an acknowledgment to the client when the file transfer is complete.
Closes the client socket.

Client (client.py)
The client connects to the server using the specified host and port. It performs the following steps:

Connects to the server.
Sends the name of the file to be transferred to the server.
Opens the file for reading.
Reads the file in chunks and sends each chunk to the server.
Waits for an acknowledgment from the server.
Closes the client socket.
