#!/usr/bin/node
// Write a script that prints x times “C is fun”
var rollingConcatenation = '';
console.group("Looping Group Example");
for (let i = 0; i<=9;i++){
     rollingConcatenation += i;
     console.log(rollingConcatenation);    
}
console.groupEnd();