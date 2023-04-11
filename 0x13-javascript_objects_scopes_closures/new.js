#!/usr/bin/node
const New = [ 4, 2, 3 ];
x = 1;
if (x in New) {
    New.push(x);
}

console.log(New);