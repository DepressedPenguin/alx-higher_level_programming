#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  const maxx = process.argv[2];
  for (i; i < maxx; i++) {
    console.log('C is fun');
  }
}
