import socket
import os
import pathlib

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8000         # Port to listen on (non-privileged ports are > 1023)


def create_file(filename, conn):
    if os.path.exists(filename):
        conn.send(b"A file with the same name already exists")
    # if pathlib.Path.is_file(filename):
    #     print("A file with the same name already exists")
    else:
        pathlib.Path(filename).touch()
        conn.sendall(b'file created')


def delete_file(filename, conn):
    if os.path.exists(filename):
        os.remove(filename)
        conn.sendall(b'file deleted')
    # if pathlib.Path.is_file(filename):
    #     pathlib.Path.unlink(filename)
    else:
        conn.sendall(b"No such file exists")


def show_contents_of(filename, conn):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            conn.sendall(f.read().encode("utf-8"))
    # if pathlib.Path.is_file(filename):
    #     with open(filename, 'r') as f:
    #         print(f.read())
    else:
        conn.sendall(b"No such file exists")


def edit_file(filename, conn):
    if os.path.exists(filename):
        with open(filename, 'w') as f:
            data = conn.recv(1024)
            print(data.decode('utf-8'))
            if data.decode('utf-8') == '#':
                return
            f.write(data.decode('utf-8'))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data.decode('utf-8'))
            if not data:
                break

            req = data.decode('utf-8').split()

            if len(req) < 2:
                conn.sendall(b"Need more info")

            match req[0][:3]:
                case 'cre':
                    create_file(req[1], conn)
                case 'del':
                    delete_file(req[1], conn)
                case 'cat':
                    show_contents_of(req[1], conn)
                case 'edi':
                    edit_file(req[1], conn)
                    conn.sendall(b'file changed')
