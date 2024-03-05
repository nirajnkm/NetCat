#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",8888))
print("Listening---")
s.listen(1)
client,addr = s.accept()
print("Connected")

while True:
    cmd = input("$ ")
    client.send(cmd.encode())
    if cmd == "exit":
        break
    output = (client.recv(1024)).decode()
    print(output)

client.close()
s.close()