#!/usr/bin/node
const args = process.argv.slice(2).map(Number).sort((a, b) => b - a);
const val = args[1] || 0;
console.log(val);
