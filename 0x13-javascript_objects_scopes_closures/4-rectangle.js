#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // An empty object
    }
  }

  print () {
    let i = 0;
    let row = '';
    let j = 0;

    while (i < this.height) {
      j = 0;
      row = '';
      while (j < this.width) {
        row += 'X';
        j++;
      }
      console.log(row);
      i++;
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
