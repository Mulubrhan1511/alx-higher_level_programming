#!/usr/bin/node
const MyDict = require('./101-data.js').dict;
const NewDict = {}
const list = []
let MyList = []
let Newlist = []

for (i in MyDict) {
    let X = MyDict[i];
    //console.log(i);
    //console.log(X);
    list.push(X);
}

//console.log(list);
MyList = [...new Set(list)];
//console.log(MyList);
MyList.sort()
const y = MyList.length;
for (x = 0; x < y; x++) {
    Newlist = [];
    //console.log(MyList[x]);
    for (j in MyDict) {
        if (MyList[x] === MyDict[j]) {
            Newlist.push(j);
        }
    }
    NewDict[MyList[x]] = Newlist;
    //console.log(Newlist);
}
console.log(NewDict);