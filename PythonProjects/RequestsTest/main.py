import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3541c8416ab366ceb80bb0e6062282fe'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

change_name = {
    "pokemon_id": "138482",
    "name": "ХлюПик"
}

add_pokeball = {
    "pokemon_id": "138482"
}

'''response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)'''

'''response_change = requests.patch(url=f'{URL}/pokemons', headers=HEADER, json=change_name)
print(response_change.text)'''

response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=add_pokeball)
print(response_catch.text)