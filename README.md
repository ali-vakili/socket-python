# socket-python
Simple python socket

## About

### How it works

**Gets client message upper case the message and then turns each character into its numeric value by also adding a value from `numbers.txt`**


```tsx
'server.py'

with open('numbers.txt', 'r') as f:
    numbers = {}
    for line in f:
        key, value = line.strip().split(':')
        numbers[int(key)] = int(value)

key = random.choice(list(numbers.keys()))
value = numbers[key]
```

**opens numbers.txt and makes a key, value dictionary of them, after that select a random key and gets its value**


```tsx
'server.py'

numeric_values = [str(ord(character) + value) for character in characters]

client_socket.send(f"{key}:{'$'.join(numeric_values)}".encode())
```

**at the end sends the key with numeric values back to the client**
