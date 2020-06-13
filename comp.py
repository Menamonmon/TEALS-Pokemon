from user import *

class Computer(User):

    def __init__(self, name, enemy=None):
        super().__init__(name, enemy)

    def set_pokemons(self):
        pok_indices = []
        while len(pok_indices) < 3:
            random_index = rd.randint(0, len(POKELIST)-1)
            if random_index not in pok_indices:
                pok_indices.append(random_index)

        self.pokemons = [POKELIST[index] for index in pok_indices]        
        [POKELIST.remove(pok) for pok in self.pokemons]        
        self.switch()

    def stats(self):
        print(f'These are the stats of the Computer ({self.name}):')
        print('These are the Pokemons of the Computer:')
        self.show_pokemons()

        print(f'This is the score of the computer: {self.score}')

    def switch(self, in_game=True):
        if not len(self.pokemons):
            print(f"\nThe Computer ({self.name}) has lost the game. None of his/her Pokemons is alive.")
            self.has_lost = True
            return False
        av_poks = copy(self.pokemons)
        if hasattr(self, 'current_pok'):
            av_poks.remove(self.current_pok)

        self.current_pok = rd.choice(av_poks)   

        if in_game:
            print(f'The player {self.name} has swtiched his current Pokemon to the following:\n')
            self.current_pok.show("*")   

        return True  
    
    def turn(self):
        self.filter_pokemons()
        command_list = copy(self.COMMANDS)
        command_list.remove("stats")
        command_list.remove('enemy-stats')
        if self.current_pok.dead:
            return self.switch()
            
        if self.current_pok.has_full_health:
            command_list.remove("heal")

        command = rd.choice(command_list)

        if len(self.pokemons) - 1 == 1:
            command_list.remove('switch')

        if command == "switch":
            self.switch()

        elif command == "heal":
            is_possible = self.current_pok.heal()
            print(f"The Computer '{self.name}' has healed his current Pokemon ({self.current_pok.name}) by 20 HP and his current HP is {self.current_pok.hp}")

        elif command == "attack":
            ap = self.current_pok.attack(self.name, self.enemy.current_pok)
            if not ap:
                print(f"The Computer's ({self.name}) did no damage.")
        else:
            raise Exception(f'The command "{command}" is not in the list of commands')

def comp_test():
    username, compname = input('What is the name of the human player?\n'), input('\nWhat name do you want to give for the computer?\n')
    user = User(username)
    enemy = Computer(compname, user)
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
    comp_test()
    