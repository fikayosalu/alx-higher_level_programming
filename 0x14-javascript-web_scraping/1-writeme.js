#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];

fs.writeFile(file, data, function (err) {
  if (err) throw err;
  console.log('file successfully created');
});
