#!/usr/bin/node

const request = require('request');
const fs = require('fs')
const file = process.argv[3]
const content = process.argv[2]

request(content, (err, response, body) => {
    if (err){
        console.log(err);
    } else {
        fs.writeFileSync(file, body);
    }
});