#!/usr/bin/node
const MyDict = require('./101-data.js').dict;
const NewDict = {}
const list = []
const MyList = []
let Newlist = []

for (i in MyDict) {
    let X = MyDict[i];
    //console.log(i);
    list.push(i);
    if (X in MyList) {
        
    } else {
        MyList.push(X);
    }
}
//console.log(list);
//console.log(MyList);
const y = MyList.length;
for (x = 0; x < y; x++) {
    Newlist = [];
    //console.log(MyList[x]);
    for (j in MyDict) {
        if (MyList[x] === MyDict[j]) {
            Newlist.push(j);
        }
    }
    NewDict[x] = Newlist;
    //console.log(Newlist);
}
console.log(NewDict);