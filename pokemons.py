from attacks import *
from inputFunctions import *

class Pokemon(object):

    def __init__(self, name, hp, max_ap, pok_type='normal'):   
        self.name = name
        self.hp = hp
        self.def_hp = self.hp
        self.max_ap = max_ap
        self.pok_type = pok_type
        self.dead = False
        self.attacks  = TypeAttack(self.pok_type) if self.pok_type != 'normal' else None

    @property
    def has_full_health(self):
        return self.hp == self.def_hp
        
    def show(self, index=0):
        print(f'{index}) A {self.pok_type} Pokemon:')
        for prop in ("name", "hp", "max_ap"):
            cap = prop.capitalize().replace("_", " ")
            print(f'        {cap}: {getattr(self, prop)}')
        
        if self.dead:
            print('*Note that this Pokemon is dead*')

    def show_attacks(self):
        if self.attacks is None:
            print("Currently, this Pokemon has no attacks.")
        else:
            for index, attack in enumerate(self.attacks.attacks, start=1):
                attack.show(1)

    def attack(self, user, enemy):
        print('\nThese are the available attacks: \n')
        self.attacks.list_attacks()
        attack_index = take_number('Type the number of the attack that you want to choose: ', 1, len(self.attacks.attacks))[0] - 1
        chosen_attack = self.attacks[attack_index]
        ap = chosen_attack.damage(enemy)
        print(f'\n{user} is attacking. {self.name} used the attack {chosen_attack.name} and inflicted {ap} damage.\n')
        enemy.take_damage(ap)
        return ap

    def heal(self):
        if self.hp >= 20:
            print("This Pokemon has full health and can not be healed anymore.")
            return False 
       
        else:
            self.hp += 20
            if self.hp > self.def_hp:
                self.hp = self.def_hp
            
            return True
            
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(f'The Pokemon {self.name} is dead :(')
            self.dead = True
        # return self.dead

    
class GrassPokemon(Pokemon):

    def __init__(self, name, hp, max_ap):
        super().__init__(name, hp, max_ap, "Grass")


class FirePokemon(Pokemon):

    def __init__(self, name, hp, max_ap):
        super().__init__(name, hp, max_ap, "Fire")


class WaterPokemon(Pokemon):

    def __init__(self, name, hp, max_ap):
        super().__init__(name, hp, max_ap, "Water")


POKEMONS = {
    'Grass': (GrassPokemon('Bulbasoar', 60, 40),
              GrassPokemon('Bellsprout', 40, 60),
              GrassPokemon('Oddish', 50, 50)),
    'Fire': ( FirePokemon('Charmainder', 25, 70),
              FirePokemon('Ninetails', 30, 50),
              FirePokemon('Ponyta', 40, 60)),
    'Water':( WaterPokemon('Squirtle', 80, 20),
              WaterPokemon('Psyduck', 70, 40),
              WaterPokemon('Polywag', 50, 50))

}

POKELIST = [  GrassPokemon('Bulbasoar', 60, 40),
              GrassPokemon('Bellsprout', 40, 60),
              GrassPokemon('Oddish', 50, 50),
              FirePokemon('Charmainder', 25, 70),
              FirePokemon('Ninetails', 30, 50),
              FirePokemon('Ponyta', 40, 60),

              WaterPokemon('Squirtle', 80, 20),
              WaterPokemon('Psyduck', 70, 40),
              WaterPokemon('Polywag', 50, 50),
              ]

def attack_test(): 
    pok1 = WaterPokemon("Polywag", 50, 50)
    pok2 = FirePokemon("Ponyta", 100, 60)
    pok1.show(1)
    pok2.show(2)
    pok1.attack("Mena", pok2)
    pok1.show(1)
    pok2.show(2)

if __name__ == "__main__":
    attack_test()