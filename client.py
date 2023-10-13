import socket

HOST = "127.0.0.1"
PORT = 12346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b"")
data = s.recv(1024)
print("Response: {}".format(data))
