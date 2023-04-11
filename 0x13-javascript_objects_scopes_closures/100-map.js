#!/usr/bin/node
const Mylist = require('./100-data.js').list;
const NewList = Mylist.map(x => x * 2);
console.log(Mylist);
console.log(NewList);