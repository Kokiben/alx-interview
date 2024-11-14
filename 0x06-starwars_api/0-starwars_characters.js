#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const movieID = process.argv[2];

async function fetchCharactersFromStarWars(movieID) {
  try {
    const apiURL = `https://swapi-api.hbtn.io/api/films/${movieID}`;
    let movieResponse = await request(apiURL);
    const characterURLs = JSON.parse(movieResponse.body).characters;

    for (const characterURL of characterURLs) {
      let characterResponse = await request(characterURL);
      const characterName = JSON.parse(characterResponse.body).name;
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

fetchCharactersFromStarWars(movieID);
