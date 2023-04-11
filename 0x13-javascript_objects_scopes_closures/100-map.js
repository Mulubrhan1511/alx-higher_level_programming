#!/usr/bin/node
const Mylist = require('./100-data.js').list;
const NewList = [];
for (i = 0; i < Mylist.length; i++) {
    NewList.push(Mylist[i] * i);
}
console.log(Mylist);
console.log(NewList);