#!/usr/bin/node

const { argv } = require('process');

/*
cript that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer:
*/

const number = parseInt(argv[2]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
