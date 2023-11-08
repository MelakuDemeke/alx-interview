#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const swapiUrl = `https://swapi.dev/api/films/${movieId}/`;

function fetchMovieCharacters() {
}

fetchMovieCharacters();
