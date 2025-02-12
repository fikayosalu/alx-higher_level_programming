#!/usr/bin/node
const request = require('request');
const id = process.argv[2]; // URL passed as an argument
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (error, response, body) => {
  if (error) {
    console.error('Error: ', error.message);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
