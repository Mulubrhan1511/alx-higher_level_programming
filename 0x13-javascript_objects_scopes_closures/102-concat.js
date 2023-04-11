#!/usr/bin/node
const MyArgs = process.argv.slice(2);
const fs = require('fs');
fs.readFile(MyArgs[0], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  //console.log(data);
  fs.readFile(MyArgs[1], 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      return;
    }
    //console.log(data2);
    str = data + data2;
    fs.writeFile(MyArgs[2], str, err => {
        if (err) {
          console.error(err);
        }
        // file written successfully
      });
  });
});