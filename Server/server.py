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
    else:
        conn.sendall(b"No such file exists")


def show_contents_of(filename, conn):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            res = f.read()
            if res == '':
                conn.sendall(b' ')
            conn.sendall(res.encode("utf-8"))
    else:
        conn.sendall(b"No such file exists")


def edit_file(filename, contents, conn):
    if os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("\n".join(contents))
        conn.sendall(b'file edited')
    else:
        conn.sendall(b'No such file exists')


try:
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

                req = data.decode('utf-8').split('\n')
                command = req[0].split()

                if len(command) < 2:
                    conn.sendall(b"Need more info")

                match command[0][:3]:
                    case 'cre':
                        create_file(command[1], conn)
                    case 'del':
                        delete_file(command[1], conn)
                    case 'cat':
                        show_contents_of(command[1], conn)
                    case 'edi':
                        print(command, req)
                        edit_file(command[1], req[1:], conn)
except Exception as e:
    print('\tAn exception occurred\n\n'+e)
