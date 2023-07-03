#!/usr/bin/node
const [arg] = process.argv.slice(2);

if (arg) {
    console.log("Arguments found");
} else {
    console.log("No argument");
}
