import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 7000))
server.listen(1)

print("Server is running...")

conn, addr = server.accept()
print("Client connected:", addr)

data = conn.recv(1024).decode()
print("Client sent:", data)

conn.sendall("Message received!".encode())

conn.close()
server.close()
