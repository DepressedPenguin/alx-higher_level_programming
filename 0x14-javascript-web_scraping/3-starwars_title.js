#!/usr/bin/node

const request = require('request');
const num = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + num, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responsej = JSON.parse(body);
    console.log(responsej.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
