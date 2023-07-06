#!/usr/bin/node
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 1));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 2));
console.log(nbOccurences(["S", 12, "c", "S", "School", 8], 12));
