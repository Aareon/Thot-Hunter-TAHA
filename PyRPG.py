import random


class Battle:
    def __init__(self, **kwargs):
        self.turn = kwargs.get('turn') or random.randint(0, 1)

    def battle(self):
        e = Enemy()
        p = Player()
        roll = random.randint(1, 100)
        while p.health > 0 or e.health > 0:
            if self.turn == 1:
                choice = input('Do you wish to carry out the battle? "1" for yes "2" for no, (W/o quotes): ')
                if choice == '1':
                    if roll == 69:
                        print('You missed!')
                    elif roll != 69:
                        print('You Hit!')
                        e.health = e.health - p.attack
                    elif choice == '2':
                        self.turn = 0
                    elif self.turn == 0:
                        if roll == 69:
                            print('The Enemy Missed!')
                            self.turn = 1
                        elif roll != 69:
                            print('The Enemy Hit!')
                            p.health = p.health - e.attack



class Player:
    player_name_opts = ('Makar', 'Joker', 'Gumball The SJW Destroyer', 'Inigo The Brave', 'Noor The Thot/Furry/SJW Hunter', 'Keemstar The Thot Obliterator', 'Hito')


    def __init__(self, **kwargs):
        self.name = kwargs.get("name") or random.choice(self.player_name_opts)
        self.level = kwargs.get("level") or 1
        self.health = self.level * 3
        if self.health == 0:
            self.health = 30
        self.attack = kwargs.get("attack") or self.level * 2

    def __repr__(self):
        return "<player(name={}, health={}, attack={}, level={})>".format(
                self.name, self.health, self.attack, self.level)

    def __str__(self):
        return "Level {} {} [HEALTH: {} | ATK: {} | Level = {}]".format(
                self.level, self.name, self.health, self.attack)


class Enemy:
    name_opts = ("Thot", "Alpha Thot", "Thot with Pumkin Spice", 'Erika Costell')

    def __init__(self, **kwargs):
        self.level = kwargs.get("level") or random.randint(1,10)
        self.name = kwargs.get("name") or random.choice(self.name_opts)
        self.defence = random.randint(10, 20) * self.level
        self.health = kwargs.get("health") or random.randint(5, 50) * self.defence / 2
        self.attack = kwargs.get("attack") or random.randint(1, 10)
        self.experience = kwargs.get("experience") or random.randint(5, 50)

    def __repr__(self):
        return "<Enemy(name={}, health={}, attack={}, defense={}, level={}) xp={}>".format(
                self.name, self.health, self.attack, self.defence,self.level, self.experience)

    def __str__(self):
        return "Level {} {} [HEALTH: {} | ATK: {} | XP: {}] ENCOUNTERED".format(
                self.level, self.name, self.health, self.attack, self.experience)


def enemy_encounter(location_level):
    b = Battle()
    b.battle()
    player = Player()
    enemy = Enemy(level=location_level)
    return enemy, player


if __name__ == "__main__":
    print(enemy_encounter(5))
