from pokemons import *

class User(object):

    def __init__(self, name):
        self.name = name

    def set_pokemons(self):
        index = 0
        for pok_type, pokemons in POKEMONS.items():
            print(f'Pokemones of type {pok_type}')
            for pokemon in enumerate(pokemons):
                pokemon.show()