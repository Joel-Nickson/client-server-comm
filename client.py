import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while 1:
        inp = input('>>> ')
        if inp.startswith('#'):
            break

        s.sendall(inp.encode('utf-8'))
        s.recv(1024)
