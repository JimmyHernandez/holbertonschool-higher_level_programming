#!/usr/bin/node
const process = require('process');
const argv = process.argv;

if (isNaN(argv[2])) {
  console.log('Not a number');
} else if (argv.length > 1) {
  const number = argv[2];
  const integer = parseInt(number);
  console.log('My number: ' + integer);
}
