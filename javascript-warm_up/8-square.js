#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const int = parseInt(argv[2]);

if (isNaN(int)) {
  console.log('Missing size');
} else {
  for (let i = 0, s; i < argv[2]; i++) {
    s = '';
      for (let j = 0; j < argv[2]; j++) {
        s += 'X';
    }
console.log(s);
    }
}
