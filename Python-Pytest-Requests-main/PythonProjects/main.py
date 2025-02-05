import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3f0e0eebcaae9c83ac177d0259bd1279'
HEADERS = {'Content-Type : application/json'}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

respons = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_create)
print(respons.text)