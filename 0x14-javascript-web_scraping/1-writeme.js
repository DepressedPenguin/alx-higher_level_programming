#!/usr/bin/node
const fs = require('fs');

function Writeme (filename, string) {
  fs.writeFile(filename, string, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}

const filename = process.argv[2];
const stringToWrite = process.argv[3];

if (!filename || !stringToWrite) {
  console.error('Usage: node script.js <filename> <string>');
  process.exit(1);
}

Writeme(filename, stringToWrite);
