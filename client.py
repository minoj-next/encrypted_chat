import socket

from cryptography.fernet import Fernet



# Define the secret key (use the same key as on the server)

key = b'nyHFaWfNUAGmCuXiI4Tu2o0Ad19SJNPflJBeX7pOhTE='

  # Replace with the key generated on the server side

cipher_suite = Fernet(key) 



# Create a socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



# Define the server's IP address and port (use the same as on the server)

server_address = ('192.168.1.5', 12345)  # Replace '192.168.1.5' with the server's IP

# Replace 12345 with the same port used on the server side



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

        cipher_suite = Fernet(key)

        encrypted_message = cipher_suite.encrypt(message.encode())

        client_socket.send(encrypted_message)



        # Receive the response from the server

        encrypted_response = client_socket.recv(1024)

        decrypted_response = cipher_suite.decrypt(encrypted_response)

        print("Server response:", decrypted_response.decode())



finally:

    # Close the client socket

    client_socket.close()
