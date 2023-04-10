#!/usr/bin/node
// Write a script that prints x times “C is fun”
if (process.argv.slice(2).length < 1) {
  console.log('Missing number of occurrences');
} else {
    for (let i = 0; i <= process.argv.slice(2).length; i++) {
        console.log('C is fun');
      }
}
