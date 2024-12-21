#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let mode = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      mode++;
    }
    i++;
  }
  return mode;
};
