import random as rd

class Attack(object):

    def __init__(self, name, power, accuracy, group, combo={}):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.group = group
        self.combo = combo

    def show(self, index=None):
        index_amend = '' if index is None else f'{index}) '
        print(f'{index_amend}A {self.group} attack:\n     Name: {self.name}\n     Power: {self.power}\n     Accuracy: {self.accuracy}%')
        if self.combo:
            print(f'     NOTE: This attack does {list(self.combo.values())[0]} more damage for enemies of type {list(self.combo.keys())[0]}')
        print()

    def damage(self, enemy):
        random_chance = rd.randint(0, 100)
        damage = 0
        if random_chance <= self.accuracy:
            damage = self.power
        else:
            print('\nThis attack was not accurate. It missed the enemy.\n')

        combo_value = self.combo[enemy.pok_type.lower()] if enemy.pok_type.lower() in self.combo else 1
        return int(damage * combo_value)


class TypeAttack(object):

    def __init__(self, pok_type):
        self.pok_type = pok_type
        self.attacks = self.set_attacks()

    def __getitem__(self, index):
        return self.attacks[index]
    
    def __len__(self):
        return len(self.attacks)

    def set_attacks(self):
        if self.pok_type.lower() == "water":
            return [Attack("Bubble", 40, 100, self.pok_type.capitalize(), {"fire": 1.5}), 
                    Attack("Hydro Pump", 185, 30, self.pok_type.capitalize(), {"fire": 1.5}),
                    Attack("Surf", 70, 90, self.pok_type.capitalize(), {"fire": 1.5})]

        elif self.pok_type.lower() == "fire":
            return [Attack("Ember", 60, 100, self.pok_type.capitalize(), {"grass": 1.5}), 
                    Attack("Fire Punch", 85, 80, self.pok_type.capitalize(), {"grass": 1.5}),
                    Attack("Flame Wheel", 70, 90, self.pok_type.capitalize(), {"grass": 1.5})]
        
        elif self.pok_type.lower() == "grass":
            return [Attack("Leaf Storm", 130, 90, self.pok_type.capitalize(), {"water": 1.5}), 
                    Attack("Mega Drain", 50, 100, self.pok_type.capitalize(), {"water": 1.5}),
                    Attack("Razor Leaf", 55, 95, self.pok_type.capitalize(), {"water": 1.5})]
        
        else:
            raise Exception(f'Invalid Pokemon type {self.pok_type}.')

    def list_attacks(self):
        for index, attack in enumerate(self.attacks, start=1):
            attack.show(index)
