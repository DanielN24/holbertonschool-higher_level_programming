#!/usr/bin/node

const { argv } = require('process');

// script that prints the first argument passed to it

if (argv.length < 3) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
