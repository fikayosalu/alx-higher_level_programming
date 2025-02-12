#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2]; // URL passed as an argument
const file = process.argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.error('Error: ', error.message);
  }
  fs.writeFile(file, body, function (err) {
    if (err) throw err;
  });
});
