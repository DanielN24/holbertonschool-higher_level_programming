#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const { argv } = require('process');

let secondBig = 0;
const argument = argv.slice(2);

if (argument.length > 1) {
  argument.sort();
  secondBig = argument[argument.length - 2];
}
console.log(secondBig);
