#!/usr/bin/node
const myArgs = process.argv.slice(2);
const fs = require('fs');
fs.readFile(myArgs[0], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const x = console.log(data);
});
console.log(x);