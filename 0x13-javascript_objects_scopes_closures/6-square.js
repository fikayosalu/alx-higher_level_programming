#!/usr/bin/node
const Parent = require('./5-square');
class Square extends Parent {
  charPrint (c) {
    let i = 0;
    let j = 0;
    let row = '';
    while (i < this.height) {
      j = 0;
      row = '';
      while (j < this.height) {
        if (c === undefined) {
          row += 'X';
        } else {
          row += c;
        }
        j++;
      }
      console.log(row);
      i++;
    }
  }
}

module.exports = Square;
