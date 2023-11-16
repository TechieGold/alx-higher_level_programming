#!/usr/bin/node

/*  a script that imports an array and computes a new array.
    A new list must be created with each value equal to the value of the initial list,
    multiplied by the index in the list.
*/
const { list } = require('./tests/100-data');

const newList = list.map((value, index) => value * index);
console.log(list);
console.log(newList);
