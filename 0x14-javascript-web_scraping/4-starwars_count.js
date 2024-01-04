#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('An error occurred. Status code:', response.statusCode);
    return;
  }

  const count = JSON.parse(body).results.reduce((acc, film) => {
    acc += film.characters.filter(char => char.includes('18')).length;
    return acc;
  }, 0);

  console.log(count);
});
