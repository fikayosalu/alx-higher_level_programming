#!/usr/bin/node
const argumentArr = process.argv;
const x = argumentArr[2];
let i = 0;
let j = 0;
let row;
if (Number(x)) {
  while (i < x) {
    j = 0;
    row = '';
    while (j < x) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
