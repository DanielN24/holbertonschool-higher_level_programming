#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) console.log(err);
  else {
    const films = JSON.parse(body).results;
    let count = 0;

    for (const filmID of films) {
      for (const character of filmID.characters) {
        // Wedge Antilles is character ID 18
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
