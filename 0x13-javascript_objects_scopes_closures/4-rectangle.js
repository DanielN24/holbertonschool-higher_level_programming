#!/usr/bin/node
// class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = 0;
    while (x < this.height) {
      x++;
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.height = this.height + this.height;
    this.width = this.width + this.width;
  }

  rotate () {
    const R = this.height;
    this.height = this.width;
    this.width = R;
  }
}
module.exports = Rectangle;
