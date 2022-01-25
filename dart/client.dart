// import 'dart:io';

// void main() {
//   Socket.connect('127.0.0.1', 4041).then((socket) {
//     socket.write('Hello, World!');
//   });
// }

import 'dart:io';
import 'dart:convert';
import 'dart:async';

void help_function() {
  print('''
    Commands available are:
        - create (filename)
        - cat (filename)
        - edit (filename)
        - delete (filename)
        ''');
}

main() async {
  var help = <String>{'!help', '--help', '-h', '!h', '/h'};
  var commands = <String>{'edit', 'create', 'cat', 'delete'};
  commands.addAll(help);

  Socket socket = await Socket.connect('127.0.0.1', 8000);
  print('connected');

  // listen to the received data event stream
  socket.listen((List<int> event) {
    print(utf8.decode(event));
  });

  String message = '';
  while (message != '#') {
    message = stdin.readLineSync() ?? '';
    if (message != '') {
      if (help.contains(message)) {
        help_function();
      } else if (commands.contains(message)) {
        socket.write(message);
      } else {
        print('Command not found');
      }
    }

    socket.write(message);
    // print(message);
  }

  // .. and close the socket
  socket.close();
}
