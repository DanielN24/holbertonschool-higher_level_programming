#!/usr/bin/node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer.
const request = require('request');
const movieID = process.argv[2];
const StarWars = 'https://swapi-api.hbtn.io/api/films/:id';

request(StarWars, movieID, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
