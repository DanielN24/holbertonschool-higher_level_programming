#!/usr/bin/node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const movieID = process.argv[2];
const StarWars = 'https://swapi-api.hbtn.io/api/films/:id';
const request = require('request');

request(`${StarWars}${movieID}`, function (err, response, body) {
  if (err) console.log(err);
  else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
