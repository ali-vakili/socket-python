import socket
import random

# Read the file and store the keys and values in a dictionary
with open('numbers.txt', 'r') as f:
    numbers = {}
    for line in f:
        key, value = line.strip().split(':')
        numbers[int(key)] = int(value)


# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

while True:
    try:
        # Wait for a connection
        print("Waiting for a connection...")
        client_socket, (client_address, client_port) = server_socket.accept()
        print(f"Client connected from {client_address}:{client_port}")

        # Receive the data in small chunks and retransmit it

        # Receive message from the client
        data = client_socket.recv(1024)

        # Upper case the message and convert it to a list of characters
        message = data.decode()

        # if len(message.strip()) == 0 or message is None:
        #     # The message is empty
        #     print("Received an empty message from the client")
        #     client_socket.close()
        # else:
        #     # The message is not empty, so do something else
        #     print("Received a message from the client:", message)
        
        message = message.upper()
        characters = []
        for character in message:
            characters.append(character)
        # characters = list(message)

        # Select a random key and find it's value
        key = random.choice(list(numbers.keys()))
        value = numbers[key]

        print('\n- selected random key is ^{}^ and recived message is \"{}\"'.format(key, message.lower()))

        # Convert the characters to their numeric values and add the value for the key
        numeric_values = [str(ord(character) + value) for character in characters]
        print(f"- the numerical values of \"{message}\" is {numeric_values}\n")

        # Send the result back to the client
        client_socket.send(f"{key}:{' '.join(numeric_values)}".encode())
        print(f"result sent to client\n")

    finally:
        # Clean up the connection
        client_socket.close()
