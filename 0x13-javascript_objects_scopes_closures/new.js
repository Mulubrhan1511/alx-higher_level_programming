#!/usr/bin/node
const myList = [1,4,5,1,2,4,5,6,7];
const unique = [...new Set(myList)];
    
console.log(unique);