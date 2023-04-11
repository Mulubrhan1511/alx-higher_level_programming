#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let m = 0;
    const x = list.length;
    for (let i = 0; i < x; i++) {
        if (list[i] === searchElement) {
            m += 1;
        }
    }
    console.log(m);
  };