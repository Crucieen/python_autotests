import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '989091815a018740e7c03f0896e3a877'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name" : "generate",
    "photo_id" : "-1"
}


response_create = requests.post(url = f'{URL}/pokemons',headers = HEADER, json = body_create)
print(response_create.text)
pokemon_id = response_create.json()['id']

body_put = {
    "pokemon_id": pokemon_id,
    "name": "Pypu",
    "photo_id": "-1"
}

response_put = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_put)
print(response_put.text)

body_pokeball = {
    "pokemon_id": pokemon_id
}
response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER, json = body_pokeball)
print(response_pokeball.text)