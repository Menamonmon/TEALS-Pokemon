from pokemons import *

class User(object):

    def __init__(self, name):
        self.name = name
        self.set_pokemons()

    def set_pokemons(self):
        index = 0
        for pok_grp_num, pokemons in enumerate(POKEMONS.items()):
            pok_type, poks = pokemons
            print(f'Pokemones of type {pok_type}:')
            for index, pokemon in enumerate(poks, start=((pok_grp_num*3)+1)):
                pokemon.show("    " + str(index))
                print()

        all_pokemons = []
        for grp in POKEMONS.values():
            all_pokemons += grp

        indices = take_number("Please type the corresponding numbers for the Pokemons that you want to choose: ", 1, len(all_pokemons), ",", 3)
        chosen_pokemons = [all_pokemons[index-1] for index in indices]
        print('Here are the Pokemons that you have chosen:\n')
        for index, p in enumerate(chosen_pokemons, start=1):
            p.show(index)

        self.pokemons = chosen_pokemons

    def choose_pokemon(self):
        

    def turn(self):
        


def user_test():
    user = User('Mena')

if __name__ == "__main__":
    user_test()
    