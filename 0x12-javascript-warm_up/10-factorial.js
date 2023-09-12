#!/usr/bin/node

function factorial (num) {
  if (Number.isNaN(num) || num < 0) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const num = Number.parseInt(process.argv[2]);

console.log(factorial(num));
