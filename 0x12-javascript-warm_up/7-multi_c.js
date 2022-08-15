#!/usr/bin/node
// script that prints x times “C is fun”

const { argv } = require('process');

const number = parseInt(argv[2]);
let x = 0;

if (isNaN(number)) {
  console.log('Missing number of occurrences');
}
for (; x < number; x++) {
  console.log('C is fun');
}
