#!/usr/bin/node
if (process.argv.length === 2 || isNaN(Math.floor(Number(process.argv[2])))) {
  console.log('Missing number of occurrences');
}
let i = 0;
while (i < process.argv[2]) {
  console.log('C is fun');
	i++;
}
