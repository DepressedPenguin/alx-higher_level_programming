#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
	if (error) {
		console.error(error);
	} else if (response.statusCode == 200){
		console.log("Code: 200");
	}
	
});
