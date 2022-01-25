import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 3000        # The port used by the server


def help_function():
    print('''
    Commands available are:
        - create (filename)
        - cat (filename)
        - edit (filename)
        - delete (filename)
        ''')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    help = {'!help', '-h', '--help'}
    commands = {'edit', 'create', 'cat', 'delete', *help}
    edit = []
    while 1:
        inp = input('>>> ')
        if inp.strip() == '':
            continue
        elif inp in help:
            help_function()
            continue
        elif inp.startswith('#'):
            break
        elif inp.startswith("edi"):
            edit = inp.split()
            while inp != "#":
                inp = input('>')
                edit.append(inp)
            inp = .join(edit[:-1])

        s.send(inp.encode('utf-8'))
        data = s.recv(1024)
        print(data.decode('utf-8'))
