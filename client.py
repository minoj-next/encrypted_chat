import socket
from cryptography.fernet import Fernet

# Define the secret key (users will provide their own key)
key = None

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Replace '0.0.0.0' and 12345 with the appropriate server address and port
server_address = ('0.0.0.0', 12345)

# Connect to the server
client_socket.connect(server_address)

try:
    while True:
        # Get user input for the message to send
        message = input("Enter a message (or 'quit' to exit): ")

        if message.lower() == 'quit':
            break  # Exit the loop if the user enters 'quit'

        # Print the message before sending it
        print("Sending:", message)

        # Send the encrypted message to the server
        if key:
            cipher_suite = Fernet(key)
            encrypted_message = cipher_suite.encrypt(message.encode())
            client_socket.send(encrypted_message)

            # Receive the response from the server
            encrypted_response = client_socket.recv(1024)
            decrypted_response = cipher_suite.decrypt(encrypted_response)
            print("Server response:", decrypted_response.decode())

        else:
            print("Error: Encryption key is missing. Please provide a valid key.")

finally:
    # Close the client socket
    client_socket.close()
