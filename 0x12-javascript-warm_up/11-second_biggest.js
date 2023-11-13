#!/usr/bin/node

/*
    A script that searches the second biggest integer in the list of arguments.

    You can assume all arguments can be converted to integer
    If no argument passed, print 0
    If the number of arguments is 1, print 0

*/
const FindSecondLargest = (...nums) => {
  if (nums.length < 2) {
    return 0;
  }

  const largest = Math.max(...nums);
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (const num of nums) {
    if (num > secondLargest && num < largest) {
      secondLargest = num;
    }
  }

  return secondLargest;
};

const numbers = process.argv.slice(2).map(Number);

if (numbers.length === 0) {
  console.log(0);
} else {
  const result = FindSecondLargest(...numbers);
  console.log(result);
}
