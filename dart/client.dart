// import 'dart:io';

// void main() {
//   Socket.connect('127.0.0.1', 4041).then((socket) {
//     socket.write('Hello, World!');
//   });
// }

import 'dart:io';
import 'dart:convert';
import 'dart:async';

main() async {
  Socket socket = await Socket.connect('127.0.0.1', 8000);
  print('connected');

  // listen to the received data event stream
  socket.listen((List<int> event) {
    print(utf8.decode(event));
  });

  String message = '';
  while (message != '#') {
    message = stdin.readLineSync() ?? '';
    socket.write(message);
  }

  // .. and close the socket
  socket.close();
}
