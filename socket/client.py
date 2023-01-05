import socket
import random

# Read the file and store the keys and values in a dictionary
with open('numbers.txt', 'r') as f:
    numbers = {}
    for line in f:
        key, value = line.strip().split(':')
        numbers[int(key)] = int(value)


# Select a random key from the dictionary
# key = random.choice(list(numbers.keys()))
# print(bytes([key]))

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('127.0.0.1', 8000)
client_socket.connect(server_address)

# Get user input for the string
message = input("Enter a message to send to the server: ")

try:
    # Send message to the server
    client_socket.send(message.encode())

    # Receive the result from the server
    result = client_socket.recv(1024)

    # Get selected key and numeric numbers of sended message from server
    key, numeric_values = result.decode().split(":")
    print(f"selceted key is {key}, numerical value of \"{message}\" is {numeric_values}")

    # Found value of selected key
    value = numbers[int(key)]
    
    # Change type of numeric number from string to int so can mines the value from them
    numeric_values = [int(number) for number in numeric_values.split()]

    # Get actuall numeric number by minesing value from each numeric then turn them into char
    characters = [chr(int(v) - value) for v in numeric_values]
    print(f"You get : {''.join(characters)}")

finally:
    # Clean up the connection
    client_socket.close()
