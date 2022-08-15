#!/usr/bin/node

const { argv } = require('process');

// script that prints two arguments passed to it, in the following format: “ is ”

if (argv.length){
    console.log(argv[2], 'is', argv[3])
}
