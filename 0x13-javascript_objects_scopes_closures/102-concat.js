#!/usr/bin/node

// a script that concats 2 files.

const fs = require('fs');
const file1Content = fs.readFileSync(process.argv[2], 'utf8');
const file2Content = fs.readFileSync(process.argv[3], 'utf8');
const concatenatedContent = file1Content + '\n' + file2Content + '\n';

fs.writeFileSync(process.argv[4], concatenatedContent);
