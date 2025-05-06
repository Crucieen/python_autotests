import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '989091815a018740e7c03f0896e3a877'
TRAINER_ID = '30810'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN, 'trainer_id' : TRAINER_ID}

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons')
    assert response.status_code == 200

def test_trainer_name():
    response_train = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_train.json()["data"][0]["trainer_id"] == TRAINER_ID

