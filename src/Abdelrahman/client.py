import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 7000))

message = "Hi Server, this is Client! | ID: 2402233 | Name: Abdelrahman Hamdy Ali"
client.sendall(message.encode())

reply = client.recv(1024).decode()
print("Server replied:", reply)

client.close()
