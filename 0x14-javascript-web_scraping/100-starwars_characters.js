#!/usr/bin/node

const request = require('request');
const userID = process.argv[2];
url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url + userID, (err, response, body) => {
    if (err) console.log(err);

    const data = JSON.parse(body);
    const chars = data.characters;

    chars.forEach(charURL => {
        request.get(charURL, (err, response, body) => {
            if (err) console.error(err);

            const charData = JSON.parse(body);
            console.log(charData.name);
        });
    });
});