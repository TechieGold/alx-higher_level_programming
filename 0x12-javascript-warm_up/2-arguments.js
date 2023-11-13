#!/usr/bin/node

/*
    A script that prints a message depending of the number of arguments passed.
    If no arguments are passed to the script, print “No argument”.
    If only one argument is passed to the script, print “Argument found”.
    Otherwise, print “Arguments found”
*/
const argNo = process.argv.length - 2;

if (argNo === 0) {
  console.log('No argument ');
} else if (argNo === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
