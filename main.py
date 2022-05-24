import requests

from flask import Flask, render_template

from flask_restful import Resource, Api

try:
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
    response.raise_for_status()
except Exception as err:
    print(f"Failed to connect to online Pokédex (error: {err}), reverting to backup...")
    raw_data = {'results': [
        {'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1/'},
        {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon/2/'},
        {'name': 'venusaur', 'url': 'https://pokeapi.co/api/v2/pokemon/3/'},
        {'name': 'charmander', 'url': 'https://pokeapi.co/api/v2/pokemon/4/'},
        {'name': 'charmeleon', 'url': 'https://pokeapi.co/api/v2/pokemon/5/'},
        {'name': 'charizard', 'url': 'https://pokeapi.co/api/v2/pokemon/6/'},
        {'name': 'squirtle', 'url': 'https://pokeapi.co/api/v2/pokemon/7/'},
        {'name': 'wartortle', 'url': 'https://pokeapi.co/api/v2/pokemon/8/'},
        {'name': 'blastoise', 'url': 'https://pokeapi.co/api/v2/pokemon/9/'},
        {'name': 'caterpie', 'url': 'https://pokeapi.co/api/v2/pokemon/10/'},
        {'name': 'metapod', 'url': 'https://pokeapi.co/api/v2/pokemon/11/'},
        {'name': 'butterfree', 'url': 'https://pokeapi.co/api/v2/pokemon/12/'},
        {'name': 'weedle', 'url': 'https://pokeapi.co/api/v2/pokemon/13/'},
        {'name': 'kakuna', 'url': 'https://pokeapi.co/api/v2/pokemon/14/'},
        {'name': 'beedrill', 'url': 'https://pokeapi.co/api/v2/pokemon/15/'},
        {'name': 'pidgey', 'url': 'https://pokeapi.co/api/v2/pokemon/16/'},
        {'name': 'pidgeotto', 'url': 'https://pokeapi.co/api/v2/pokemon/17/'},
        {'name': 'pidgeot', 'url': 'https://pokeapi.co/api/v2/pokemon/18/'},
        {'name': 'rattata', 'url': 'https://pokeapi.co/api/v2/pokemon/19/'},
        {'name': 'raticate', 'url': 'https://pokeapi.co/api/v2/pokemon/20/'}
    ]}
else:
    print(f"Successfully fetched {len(response.json()['results'])} Pokemon from Pokédex.")
    raw_data = response.json()

pokemon = [{"name": x['name'], "id": x['url'].split("/")[-2]} for x in raw_data['results']]

app = Flask(__name__)
api = Api(app)

class PokemonList(Resource):
    def get(self):
        return {"count": len(pokemon), "results": pokemon}, 200

class Pokemon(Resource):
    def get(self, id):
        result = [d for d in pokemon if d['id'] == str(id)][0]
        print(id, result)
        return result, 200

api.add_resource(PokemonList, '/pokemon')
api.add_resource(Pokemon, '/pokemon/<int:id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
