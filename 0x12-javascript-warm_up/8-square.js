#!/usr/bin/node
const size = process.argv[2];
if (isNaN(Math.floor(Number(size)))) {
  console.log('Missing size');
} else {
  let i = 0;
  while(i < size) {
    console.log('X'.repeat(size));
    i++;
  }
}
