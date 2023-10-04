import socket
from cryptography.fernet import Fernet

# Generate a secret key for encryption (server-side)
key = Fernet.generate_key()
print("Generated Key:", key.decode())  # Print the key
cipher_suite = Fernet(key)

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('0.0.0.0', 12345)  # Replace '0.0.0.0' with the your system IP
# Replace 12345 with the same port used on the client side

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Waiting for a connection...")
connection, client_address = server_socket.accept()

try:
    print("Connection established with", client_address)

    while True:
        # Receive the encrypted message from the client
        encrypted_message = connection.recv(1024)

        # Decrypt the message
        decrypted_message = cipher_suite.decrypt(encrypted_message)

        # Print the received message
        print("Received:", decrypted_message.decode())

        # Prompt the server to enter a message
        server_input = input("Server: Enter a message (or 'quit' to exit): ")
        
        # Check if the server wants to quit
        if server_input.lower() == 'quit':
            break

        # Encrypt and send the server's message to the client
        encrypted_response = cipher_suite.encrypt(server_input.encode())
        connection.send(encrypted_response)

finally:
    connection.close()
