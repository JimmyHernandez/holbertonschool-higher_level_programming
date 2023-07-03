#!/usr/bin/node
const process = require('process');
const argv = process.argv;
let count = 0;
//getting length
if (argv !== null) {
    for (count in argv) { count++; }
}
//conditions
if (count < 3) {
    console.log("No argument");
} else if (count === 3) {
    console.log("Argument found");
} else {
    console.log("Arguments found")
}
