import socket

HOST = "127.0.0.1"
PORT = 5500

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server.\nType something to search (or 'quit' to exit):")

    while True:
        msg = input("> ").strip()
        if msg.lower() == "quit":
            break
        s.sendall(msg.encode())
        response = s.recv(1024).decode()
        print("Response:", response)