#!/usr/bin/node
const argumentArr = process.argv;
function add (a, b) {
  a = Number(argumentArr[2]);
  b = Number(argumentArr[3]);
  console.log(a + b);
}
add();
