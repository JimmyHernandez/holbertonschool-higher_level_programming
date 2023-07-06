#!/usr/bin/node
const newSquare = require('./5-square');

class Square extends newSquare {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let I = 0; I < this.height; I++) {
      let S = '';
      for (let J = 0; J < this.width; J++) {
        S += c;
      }
      console.log(S);
    }
  }
}

module.exports = Square;
