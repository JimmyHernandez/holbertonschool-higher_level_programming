#!/usr/bin/node
let pos = 0;
exports.logMe = function (item) {
    console.log(pos + ': ' + item);
    pos++;
};
