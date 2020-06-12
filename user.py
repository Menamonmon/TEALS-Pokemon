from pokemons import *

class User(object):
    COMMANDS = ["switch", "heal", "attack", "stats"]

    def __init__(self, name, enemy=None):
        self.name = name
        self.score = 0
        self.has_lost = False
        self.enemy = enemy
        if self.enemy is not None:
            self.enemy.enemy = self

        self.set_pokemons()

    def show_my_pokemons(self, pok_list=None):
        if not pok_list:
            pok_list = self.pokemons

        for index, pok in enumerate(pok_list, start=1):
            pok.show(f"    {index}")

    def set_pokemons(self):
        for pok_grp_num, pokemons in enumerate(POKEMONS.items()):
            pok_type, poks = pokemons
            print(f'Pokemones of type {pok_type}:')
            for index, pokemon in enumerate(poks, start=((pok_grp_num*3)+1)):
                pokemon.show(f'    {index}')
                print()

        indices = take_number("Please type the corresponding numbers for the Pokemons that you want to choose: ", 1, len(POKELIST), ",", 3)
        chosen_pokemons = [POKELIST[index-1] for index in indices]
        print('Here are the Pokemons that you have chosen:\n')
        self.pokemons = chosen_pokemons

        self.switch(False)

    def switch(self, in_game=True):
        if not len(self.pokemons):
            print("\nYou lost the game because none of your Pokemons is alive :(\n")
            self.has_lost = True
            return False
        
        self.show_my_pokemons()

        current_pok_index = take_number("\nWhich Pokemon of the above do you want to choose as your current Pokemon: ", 1, len(POKELIST))[0] - 1
        self.current_pok = self.pokemons[current_pok_index]        
        
        if in_game:
            print(f'The player {self.name} has swtiched his current Pokemon to the following:\n')
            self.current_pok.show()

        return True

    def filter_pokemons(self):
        for pok in self.pokemons:
            if pok.dead:
                self.pokemons.remove(pok)

    def stats(self):
        print(f'Here are the stats for {self.name}')
        print('\nThese are your Pokemons: ')
        self.show_my_pokemons()
        print(f'Your current score is {self.score}.')
    
    def turn(self):
        self.filter_pokemons()
        if self.current_pok.dead:
            print(f'\n{self.name}! Your current Pokemon is dead. You can only switch to another Pokemon in this turn.\n')
            return self.switch()

        while True:
            command = take_command(f"""\nThis is your turn {self.name}. You can use one of the four following commands:
            stats: shows your score and the status of all of your pokemons
            heal  : heals the current Pokemon by 20 HP
            attack: attacks the current Pokemon of your enemy (damage value is random)
            switch: change the current Pokemon to another one
            Type the command here: """, self.COMMANDS)

            if command == "switch":
                return self.switch()

            elif command == "stats":
                self.stats()
                continue

            elif command == "heal":
                is_possible = self.current_pok.heal()
                if not is_possible:
                    continue
                    
                return is_possible

            elif command == "attack":
                self.score += self.current_pok.attack(self.name, self.enemy.current_pok)
                return 

            else:
                raise Exception(f'The command "{command}" is not in the list of commands')



def user_test():
    user = User('Mena')
    enemy = User('Masio', user)
    while True:
        user.turn()
        if enemy.has_lost:
            print(f'The Player {enemy.name} has lost.')
            break
        enemy.turn()
        
        if user.has_lost:
            print(f'The Player {user.name} has lost.')
            break
            
        

if __name__ == "__main__":
    user_test()
    