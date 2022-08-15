#!/usr/bin/node

const { argv } = require('process');

let secondBig = 0;
const argument = argv.slice(2);

if (argument.length > 1) {
  argument.sort();
  secondBig = argument[argument.length - 2];
}
console.log(secondBig);
