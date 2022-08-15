#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: “ is ”
import { argv } from 'process';
if (argv.length){
    console.log(argv[2], ' is ', argv[3]);
}
