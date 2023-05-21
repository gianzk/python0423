
import requests


urlBase='https://pokeapi.co/api/v2/'



urlView=f'{urlBase}pokemon?limit=100000&offset=0'

response = requests.get(urlView)
data=response.json()
listPokemons=data['results']

for i,pokemon in enumerate(listPokemons):
    pokename=pokemon['name']
    print(f'{i+1}-{pokename}')

pokemonIndex=int(input('ingrese el pokemon que necesita la info'))

urlNumber=f'pokemon/{pokemonIndex}/'

urlDetail=f'{urlBase}{urlNumber}'


response = requests.get(urlDetail)
data2=response.json()

print("esta es la info del pokemon",data2)


