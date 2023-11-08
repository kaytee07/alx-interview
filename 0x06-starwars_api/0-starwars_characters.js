#!/usr/bin/node

var arguments = process.argv;
if (arguments.length !== 3) return;
const request = require('request');

async function get_character(characters, index) {
    if (characters.length === index) return;

    request(characters[index], function (error, response, body) {
        if (error) {
            console.error('Error:', error);
            return;
        }
        try {
            let to_json = JSON.parse(body);
            console.log(to_json['name']);
        } catch (parseError) {
            console.error('Error parsing JSON:', parseError);
        }
        
        index += 1;
        get_character(characters, index);
    });
}

request(`https://swapi-api.alx-tools.com/api/films/${arguments[2]}`, function (error, response, body) {
    if (error) {
        console.error('Error:', error);
        return;
    }
    try {
        const json = JSON.parse(body);
        get_character(json['characters'], 0);
    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
    }
});

