#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const films = JSON.parse(body).results;
  const numMovies = films.filter((film) => {
    return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
  }).length;

  console.log(numMovies);
});
