#!/usr/bin/node


const dict = {
    89: 1,
    90: 2,
    91: 1,
    92: 3,
    93: 1,
    94: 2
  };
const NewDict = { '1': [ '89', '91', '93' ], '2': [ '90', '94' ], '3': [ '92' ] }
const Mule = {}
NewDict[1].unshift(100);
console.log(NewDict);
const m = [ '89', '91', '93' ];
const k = 1;
Mule[2] = m;
console.log(Mule);
