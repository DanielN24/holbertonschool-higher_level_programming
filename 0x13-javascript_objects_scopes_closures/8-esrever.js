#!/usr/bin/node
// function that returns the reversed version of a list
exports.esrever = function (list) {
  const a = [];
  for (let i = 0; i < list.length; i++) {
    a.unshift(list[i]);
  }
  return a;
};
