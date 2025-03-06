import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'Token'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}

'''body_creat_pokemon = {
    "name": "Саша",
    "photo_id": 1
}'''

'''body_change = {
    "pokemon_id": "250245",
    "name": "Миша",
    "photo_id": 1
}'''

body_add_pokeball = {
    "pokemon_id": "250245"
}

'''response = requests.post(url = f'{URL}/pokemons',headers = HEADER,json = body_creat_pokemon)
print(response.text)'''


'''response = requests.put(url = f'{URL}/pokemons',headers = HEADER,json = body_change)
print(response.text)'''

response = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER,json = body_add_pokeball)
print(response.text)
