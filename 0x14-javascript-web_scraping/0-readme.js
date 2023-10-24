#!/usr/bin/node
const fs = require('fs');

function read_inside_file(filename) {
  fs.readFile(filename, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
const filename = process.argv[2];
read_inside_file(filename);
