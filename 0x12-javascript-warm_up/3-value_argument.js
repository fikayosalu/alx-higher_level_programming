#!/usr/bin/node
const argumentArr = process.argv;
if (argumentArr.length <= 2) {
  console.log('No argument');
} else {
  console.log(argumentArr[2]);
}
