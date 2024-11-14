#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

// Star Wars API endpoint for films
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// First, fetch the movie data
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Print each character's name in the order they appear in the "characters" list
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
