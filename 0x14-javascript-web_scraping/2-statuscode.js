#!/usr/bin/node

const request = require('request');

let url = 'https://alx-intranet.hbtn.io/status';

request(url, (error, response, body) => {
	if (error) {
		console.error(error);
	} else {
		if (response.statusCode === 200) {
			console.log("Code: 200");
		} else {
			console.log("Code: 404");
		}
	}
});
