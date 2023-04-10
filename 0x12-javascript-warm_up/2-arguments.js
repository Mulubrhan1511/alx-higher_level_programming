#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments passed
const arguments = process.argv.slice(2);
if (arguments.length < 1) {
    //  If no arguments are passed to the script, print “No argument”
    console.log('No argument');
  } else if (arguments.length == 1) {
    //  If only one argument is passed to the script, print “Argument found”
    console.log('Argument found');
  } else {
    //  Otherwise, print “Arguments found”
    console.log('Arguments found');
  }
