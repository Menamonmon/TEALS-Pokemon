from user import *

class Computer(User):

    def __init__(self, name, enemy=None):
        super().__init__(name, enemy)

    def set_pokemons(self):
        pok_indices = []
        while len(pok_indices) < 3:
            random_index = rd.randint(0, 8)
            if random_index not in pok_indices:
                pok_indices.append(random_index)

        self.pokemons = [POKELIST[index] for index in pok_indices]        
        self.switch(False)

    def switch(self, in_game=True):
        if not len(self.pokemons):
            print(f"\nThe Computer ({self.name}) has lost the game. None of his/her Pokemons is alive.")
            self.has_lost = True
            return False

        self.current_pok = rd.choice(self.pokemons)   

        if in_game:
            print(f'The player {self.name} has swtiched his current Pokemon to the following:\n')
            self.current_pok.show()   

        return True  
    
    def turn(self):
        command_list = self.COMMANDS
        command_list.remove("stats")
        if self.current_pok.dead:
            return self.switch()
            
        if self.current_pok.has_full_health:
            command_list.remove("heal")

        command = rd.choice(command_list)

        if command == "switch":
            self.switch()

        elif command == "heal":
            is_possible = self.current_pok.heal()
            print(f"The Computer '{self.name}' has healed his current Pokemon ({self.current_pok.name}) by 20 HP and his current HP is {self.current_pok.hp}")

        elif command == "attack":
            self.score += self.current_pok.attack(self.name, self.enemy.current_pok)

        else:
            raise Exception(f'The command "{command}" is not in the list of commands')

def comp_test():
    user = User('Mena')
    enemy = Computer('Masio', user)
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
    