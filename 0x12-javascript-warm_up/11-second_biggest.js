#!/usr/bin/node

let secondBig = 0;
const argument = process.argv.slice(2);

if (argument.length > 1) {
  argument.sort();
  secondBig = argument[argument.length - 2];
}
console.log(secondBig);
