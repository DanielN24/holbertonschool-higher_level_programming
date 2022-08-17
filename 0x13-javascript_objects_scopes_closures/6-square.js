#!/usr/bin/node
const Rectangle = require('./4-rectangle');
// class Square that defines a square
// and inherits from Rectangle of 4-rectangle.js
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      let i = 0;
      while (i < this.width) {
        i++;
        console.log(c.repeat(this.height));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
