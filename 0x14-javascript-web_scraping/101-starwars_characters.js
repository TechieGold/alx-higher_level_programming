#!/usr/bin/node

const request = require('request');
const userID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + userID, (err, response, body) => {
  if (!err) {
    const chars = JSON.parse(body).characters;

    chars.forEach((charURL, index) => {
      request(charURL, (err, response, body) => {
        if (!err) console.log(JSON.parse(body).name);

        if (index === chars.length - 1);
      });
    });
  }
});
