import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while 1:
        inp = input('>>> ')
        if inp.strip() == '':
            continue
        if inp.startswith('#'):
            break
        if inp.startswith("edit"):
            while inp != "#":
                s.send(inp.encode('utf-8'))
                data = s.recv(1024)
                inp = input('>')

        s.send(inp.encode('utf-8'))
        data = s.recv(1024)
        print(data.decode('utf-8'))
