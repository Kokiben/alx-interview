#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const movieID = process.argv[2];

async function fetchStarWarsCharacters(movieID) {
  try {
    const apiURL = `https://swapi-api.hbtn.io/api/films/${movieID}`;
    const movieResponse = await request(apiURL);
    const characterURLs = JSON.parse(movieResponse.body).characters;

    // Fetch each character's name in the specified order
    for (const characterURL of characterURLs) {
      const characterResponse = await request(characterURL);
      const characterName = JSON.parse(characterResponse.body).name;
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

fetchStarWarsCharacters(movieID);
