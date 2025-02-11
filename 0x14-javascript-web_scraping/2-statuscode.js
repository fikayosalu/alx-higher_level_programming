#!/usr/bin/node
const request = require('request');
const url = process.argv[2]; // URL passed as an argument

request(url, (error, response, body) => {
  if (error) {
    console.error('Error: ', error.message);
  }
  console.log('code:', response.statusCode);
});
