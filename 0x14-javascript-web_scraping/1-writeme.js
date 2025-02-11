#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];

if (!file || data === undefined) {
  console.error('Usage: node 1-writeme.js <filename> <content>');
  process.exit(1);
}

fs.writeFile(file, data, function (err) {
  if (err) throw err;
});
