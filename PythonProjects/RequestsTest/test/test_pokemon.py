import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bc3098395ad60b79d41f9aaff693652c'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}
TRAINER_ID = 22790

def test_status_code ():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response.status_code == 200 


def test_name_trainers ():
     response_get = requests.get(url=f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
     assert response_get.json()["data"][0]["name"] == 'Миша'


   
