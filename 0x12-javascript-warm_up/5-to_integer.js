#!/usr/bin/node
const argumentArr = process.argv;
if (Number(argumentArr[2])) {
  console.log(`My number: ${Number(argumentArr[2])}`);
} else {
  console.log('Not a number');
}
