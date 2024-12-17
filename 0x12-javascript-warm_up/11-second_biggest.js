#!/usr/bin/node
const argumentArr = process.argv;
let max = Number.NEGATIVE_INFINITY;
let secondMax = Number.NEGATIVE_INFINITY;
let i = 0;
let j = 0;
if (argumentArr.length <= 3) {
  console.log(0);
} else {
  while (i < argumentArr.length) {
    if (max < argumentArr[i]) {
      max = argumentArr[i];
    }
    i++;
  }
  while (j < argumentArr.length) {
    if (secondMax < argumentArr[j] && argumentArr[j] < max) {
      secondMax = argumentArr[j];
    }
    j++;
  }
  console.log(secondMax);
}
