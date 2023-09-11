#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Undefined is undefined');
} else {
  console.log(process.argv[2], process.argv[3]);
}
