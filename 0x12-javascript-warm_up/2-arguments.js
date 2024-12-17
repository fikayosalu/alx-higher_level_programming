#!/usr/bin/node
const argumentArr = process.argv;
if (argumentArr.length <= 2) {
  console.log('No argument');
} else if (argumentArr.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
