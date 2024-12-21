#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length - 1;
  const revArr = [];
  while (i >= 0) {
    revArr.push(list[i]);
    i--;
  }
  return revArr;
};
