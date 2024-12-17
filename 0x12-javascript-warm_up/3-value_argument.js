#!/usr/bin/node
const argumentArr = process.argv;
if (argumentArr[2]) {
  console.log(argumentArr[2]);
} else {
  console.log('No argument');
}
