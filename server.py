import socket
from cryptography.fernet import Fernet

# Replace '0.0.0.0' with the appropriate server address
server_address = ('0.0.0.0', 12345)
cipher_suite = None  # Users will provide their own encryption key

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

print("Waiting for a connection...")
connection, client_address = server_socket.accept()

try:
    print("Connection established with", client_address)

    while True:
        # Receive the encrypted message from the client
        encrypted_message = connection.recv(1024)

        # Decrypt the message if a key is provided
        if cipher_suite:
            decrypted_message = cipher_suite.decrypt(encrypted_message)
            print("Received:", decrypted_message.decode())

        # Prompt the server to enter a message
        server_input = input("Server: Enter a message (or 'quit' to exit): ")

        # Check if the server wants to quit
        if server_input.lower() == 'quit':
            break

        # Encrypt and send the server's message to the client
        if cipher_suite:
            encrypted_response = cipher_suite.encrypt(server_input.encode())
            connection.send(encrypted_response)

finally:
    connection.close()
