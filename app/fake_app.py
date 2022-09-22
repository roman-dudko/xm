from flask import Flask, jsonify
from random import randrange
from time import sleep
import sys

person_fake_data = {
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": "19BBY",
    "gender": "male",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "films": [
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/6/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/7/"
    ],
    "species": [
        "https://swapi.dev/api/species/1/"
    ],
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/",
        "https://swapi.dev/api/vehicles/30/"
    ],
    "starships": [
        "https://swapi.dev/api/starships/12/",
        "https://swapi.dev/api/starships/22/"
    ],
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-20T21:17:56.891000Z",
    "url": "https://swapi.dev/api/people/person_id/"
}

planet_fake_data = {
    "name": "Yavin IV",
    "rotation_period": "24",
    "orbital_period": "4818",
    "diameter": "10200",
    "climate": "temperate, tropical",
    "gravity": "1 standard",
    "terrain": "jungle, rainforests",
    "surface_water": "8",
    "population": "1000",
    "residents": [],
    "films": [
        "https://swapi.dev/api/films/1/"
    ],
    "created": "2014-12-10T11:37:19.144000Z",
    "edited": "2014-12-20T20:58:18.421000Z",
    "url": "https://swapi.dev/api/planets/3/"
}

starship_fake_data = {
    "name": "Death Star",
    "model": "DS-1 Orbital Battle Station",
    "manufacturer": "Imperial Department of Military Research, Sienar Fleet Systems",
    "cost_in_credits": "1000000000000",
    "length": "120000",
    "max_atmosphering_speed": "n/a",
    "crew": "342,953",
    "passengers": "843,342",
    "cargo_capacity": "1000000000000",
    "consumables": "3 years",
    "hyperdrive_rating": "4.0",
    "MGLT": "10",
    "starship_class": "Deep Space Mobile Battlestation",
    "pilots": [],
    "films": [
        "https://swapi.dev/api/films/1/"
    ],
    "created": "2014-12-10T16:36:50.509000Z",
    "edited": "2014-12-20T21:26:24.783000Z",
    "url": "https://swapi.dev/api/starships/9/"
}

sys.path.append('../../')
app = Flask(__name__)


@app.route('/people/<person_id>', methods=['GET'])
def get_people(person_id):
    if not person_id.isnumeric():
        return jsonify("400 Person ID should be positive integer"), 400
    if int(person_id) in range(101):
        sleep_time = float(randrange(1, 99)) / 100
        sleep(sleep_time)
        return jsonify(person_fake_data)
    else:
        return jsonify(f"404 Person with ID={person_id} is not found"), 404


@app.route('/planets/<planet_id>', methods=['GET'])
def get_planet(planet_id):
    if not planet_id.isnumeric():
        return jsonify("400 Planet ID should be positive integer"), 400
    if int(planet_id) in range(101):
        return jsonify(planet_fake_data)
    else:
        return jsonify(f"404 Planet with ID={planet_id} is not found"), 404


@app.route('/starships/<starship_id>', methods=['GET'])
def get_starship(starship_id):
    if not starship_id.isnumeric():
        return jsonify("400 Starship ID should be positive integer"), 400
    if int(starship_id) in range(101):
        return jsonify(starship_fake_data)
    else:
        return jsonify(f"404 Starship with ID={starship_id} is not found"), 404


app.run(port=5000, debug=True)
