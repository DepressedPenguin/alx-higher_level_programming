#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const result = a + b;
    console.log(result);
  }
}

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

add(num1, num2);
