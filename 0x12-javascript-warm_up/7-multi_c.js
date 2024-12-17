#!/usr/bin/node
const argumentArr = process.argv;
let i = 0;
const x = argumentArr[2];
if (Number(x)) {
  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
