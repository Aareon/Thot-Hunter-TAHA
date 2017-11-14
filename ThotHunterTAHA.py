import random

class Battle:
    def __init__(self, **kwargs):
        self.turn = kwargs.get('turn') or random.randint(0,1)
    def battle(self):
        roll = random.randint(1, 100)
        if self.turn == 1:
            choice = input('Do you wish to carry out the battle? "1" for yes "2" for no, (W/o quotes)')
            if choice == '1':
                if roll == 69:
                    print('You missed!')
                elif roll != 69:
                    print('You Hit!')
                    Enemy.health = Enemy.health - Player.attack
            elif choice == '2':
                self.turn = 0
        elif self.turn == 0:
            if roll == 69:
                print('The Enemy Missed!')
                self.turn = 1
            elif roll != 69:
                print('The Enemy Hit!')
                Player.health = Player.health - Enemy.attack


class Player:
    player_name_opts = ('Makar', 'Joker', 'Gumball The SJW Destroyer', 'Inigo The Brave', 'Noor The Thot/Furry/SJW Hunter', 'Keemstar The Thot Obliterator', 'Hito')
    def __init__(self, **kwargs):
        self.name = kwargs.get("name") or random.choice(self.player_name_opts)
        self.level = kwargs.get("level") or 1
        self.health = self.level * 3
        self.experience = 0
        if self.health == 0:
            self.health = 30
        self.attack = kwargs.get("attack") or self.level * 2
        if self.experience == self.experience + 100 * self.level:
            self.experience = self.level + 1

    def __repr__(self):
        return "<player(name={}, health={}, attack={}, level={})>".format(
                self.level, self.pname, self.health, self.attack)

    def __str__(self):
        return "Level {} {} [HEALTH: {} | ATK: {} | Level = {}]".format(
                self.level, self.name, self.health, self.attack)

class Enemy:
    name_opts = ("Thot", "Alpha Thot", "Thot with Pumkin Spice", 'Erika Costell')
    def __init__(self, **kwargs):
        self.name = kwargs.get("name") or random.choice(self.name_opts)
        self.health = kwargs.get("health") or random.randint(5, 50)
        self.attack = kwargs.get("attack") or random.randint(1, 10)
        self.experience = kwargs.get("experience") or random.randint(5, 50)
        level = kwargs.get("level")
        if level is not None:
            level = random.randint(level - 2, level + 2)

    def __repr__(self):
        return "<Enemy(name={}, health={}, attack={}, defense={}, level={}) xp={}>".format(
                self.name, self.health, self.attack, self.level, self.experience)

    def __str__(self):
        return "Level {} {} [HEALTH: {} | ATK: {} | XP: {}] ENCOUNTERED".format(
                self.level, self.name, self.health, self.attack, self.experience)




def enemy_encounter(location_level):
    player = Player()
    enemy = Enemy(level=location_level)
    return enemy, player


if __name__ == "__main__":
    print(enemy_encounter(5))
