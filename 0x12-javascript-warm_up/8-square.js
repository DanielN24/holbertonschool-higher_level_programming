#!/usr/bin/node
// script that prints a square

const { argv } = require('process');

const number = parseInt(argv[2]);

if (isNaN(number)) {
  console.log('Missing size');
}
for (let x = 0; x < number; x++) {
  console.log('X'.repeat(number));
}
