#!/usr/bin/node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer.
const request = require('request');
const StarWars = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(StarWars, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
