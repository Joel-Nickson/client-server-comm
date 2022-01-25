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

  Socket socket = await Socket.connect('127.0.0.1', 8000);
  print('connected');

  // listen to the received data event stream
  socket.listen((List<int> event) {
    print(utf8.decode(event));
  });

  String message = '';
  List edit = [], msg_split = [];
  do {
    stdout.write('>>> ');
    message = stdin.readLineSync() ?? '';
    msg_split = message.split(" ");

    if (help.contains(msg_split[0])) {
      help_function();
      continue;
    } else if (!commands.contains(msg_split[0])) {
      print('Command not recognized');
      continue;
    } else if (commands.contains(msg_split[0]) && msg_split.length < 2) {
      print('Not enough arguments to perform any operation');
      continue;
    } else if (msg_split[0] == "edit") {
      while (message != '#') {
        edit.add(message);
        stdout.write('> ');
        message = stdin.readLineSync() ?? '';
      }
      message = edit.join('\n');
    }

    socket.add(utf8.encode(message));
    await Future.delayed(Duration(milliseconds: 500));
  } while (message != '#');

  print('Bye');
  socket.close();
}
