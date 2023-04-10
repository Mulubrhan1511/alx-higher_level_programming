#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments passed
if (process.argv.slice(2).length < 1) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
  