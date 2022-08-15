#!/usr/bin/node
// function that executes x times a function.
exports.callMeMoby = function (x, theFunction) {
  let y = 0;
  for (; y < x; y++) {
    theFunction();
  }
};
