#!/usr/bin/node
/*
const { argv } = require('process');

if (argv.length < 3) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
*/
const argument = process.argv[2];
if (argument === undefined) {
  console.log('No argument');
} else {
  console.log(argument);
}
