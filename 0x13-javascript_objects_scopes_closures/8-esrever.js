#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  let y = 0;
  const listx = [];
  for (i = list.length - 1; i >= 0; i--) {
    listx[y] = list[i];
    y++;
  }
  return listx;
};
