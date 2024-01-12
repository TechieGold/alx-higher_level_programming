#!/usr/bin/node

const request = require('request');
const episodeN = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + episodeN, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJson = JSON.parse(body);
    console.log(responseJson.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
