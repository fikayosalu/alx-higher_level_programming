#!/usr/bin/node
const argumentArr = process.argv;
let max = Number.NEGATIVE_INFINITY;
let secondMax = Number.NEGATIVE_INFINITY;
let i = 2;
if (argumentArr.length <= 3) {
  console.log(0);
} else {
  while (i < argumentArr.length) {
    const num = Number(argumentArr[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
    i++;
  }
  console.log(secondMax);
}
