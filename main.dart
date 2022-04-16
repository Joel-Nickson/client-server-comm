// use this in the flutter app main.dart file

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:rflutter_alert/rflutter_alert.dart';

void main() => runApp(RatelApp());

class RatelApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text('C_S Comm'),
        ),
        body: PopupDialog(),
      ),
    );
  }
}

class PopupDialog extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
              child: Text('Create'),
              onPressed: () => _onAlertWithCustomContentPressed(
                context,
                "Create",
                "File created Successfully",
                false,
              ),
            ),
            ElevatedButton(
              child: Text('Edit'),
              onPressed: () => _onAlertWithCustomContentPressed(
                context,
                "Edit",
                "File edit completed Successfully",
                true,
              ),
            ),
            ElevatedButton(
              child: Text('Show'),
              onPressed: () => _onAlertWithCustomContentPressed(
                context,
                "Show",
                "File \nedit completed \nSuccessfully",
                false,
              ),
            ),
            ElevatedButton(
              child: Text('Delete'),
              onPressed: () => _onAlertWithCustomContentPressed(
                context,
                "Delete",
                "File deleted Successfully",
                false,
              ),
            ),
          ],
        ),
      ),
    );
  }

  // Alert custom content
  _onAlertWithCustomContentPressed(context, title, desc, optional) {
    Alert(
      context: context,
      title: title,
      content: Column(
        children: <Widget>[
          TextField(
            decoration: InputDecoration(
              icon: Icon(Icons.account_circle),
              labelText: 'File Name',
            ),
          ),
          if (optional == true)
            TextField(
              decoration: InputDecoration(
                icon: Icon(Icons.lock),
                labelText: 'Text',
              ),
            ),
        ],
      ),
      buttons: [
        DialogButton(
          onPressed: () => Alert(
            context: context,
            title: "$title",
            desc: desc,
          ).show(),
          child: Text(
            title,
            style: TextStyle(color: Colors.white, fontSize: 20),
          ),
        )
      ],
    ).show();
  }
}
