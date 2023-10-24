#!/usr/bin/node
const fs = require('fs');

function write_me(filename, string) {
  fs.writeFile(filename, string, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
  });
}

const filename = process.argv[2];
const stringToWrite = process.argv[3];

if (!filename || !stringToWrite) {
  console.error('Usage: node script.js <filename> <string>');
  process.exit(1);
}

write_me(filename, stringToWrite);

