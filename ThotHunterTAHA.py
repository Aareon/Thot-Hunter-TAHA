import random

turn = None
choice = 0

class Player:
    player_name_opts = ('Makar', 'Joker', 'Gumball The SJW Destroyer', 'Inigo The Brave', 'Noor The Thot/Furry/SJW Hunter', 'Erika Costell The Snake', 'Keemstar The Thot Obliterator')
    def __init__(self, **kwargs):
        self.name = kwargs.get("name") or random.choice(self.player_name_opts)
        self.level = kwargs.get("level") or 0
        self.health = self.level * 3
        self.attack = kwargs.get("attack") or self.level * 2

    def __repr__(self):
        return "<player(name={}, health={}, attack={}, level={})>".format(
                self.level, self.pname, self.health, self.attack)

    def __str__(self):
        return "Level {} {} [HEALTH: {} | ATK: {} | Level = {}]".format(
                self.level, self.name, self.health, self.attack)

    def attack():
        global turn
        global choice
        if turn == 1:
            choice = input('Type 1 or 2 in order to either attack or skip the turn: ')
        elif choice == '2':
            turn = 1
        elif choice == '1':
            roll = random.randint(1, 100)
            if roll == 69:
                print('You missed!')
                turn = 1
            elif not roll == 69:
                print('You Hit!')
                Enemy.health = Enemy.health - Player.attack
                print(f'The Enemy now has {Enemy.health}!')

class Enemy:
    name_opts = ("Thot", "Alpha Thot", "Thot with Pumkin Spice", 'Erika Costell')
    def __init__(self, **kwargs):
        self.name = kwargs.get("name") or random.choice(self.name_opts)
        self.health = kwargs.get("health") or random.randint(5, 50)
        self.attack = kwargs.get("attack") or random.randint(1, 10)
        self.experience = kwargs.get("experience") or random.randint(5,50)
        level = kwargs.get("level")
        if level is not None:
            level = random.randint(level - 2, level + 2)
        self.level = level

    def __repr__(self):
        return "<Enemy(name={}, health={}, attack={}, defense={}, level={}) xp={}>".format(
                self.name, self.health, self.attack, self.defense, self.level, self.experience)

    def __str__(self):
        return "Level {} {} [HEALTH: {} | ATK: {} | XP: {}] ENCOUNTERED".format(
                self.level, self.name, self.health, self.attack, self.experience)
    def attack():
            roll = random.randint(1, 100)
            if turn == 1:
                if roll == 69:
                    print('The enemy missed missed!')
                elif not roll == 69:
                    print('The enemy Hit!')
                    Enemy.health = Player.health - Enemy.attack
                    print(f'you lost {enemy.attack} health!')


def enemy_encounter(location_level):
    global turn
    turn = random.randint(1, 2)
    enemy = Enemy(level=location_level)
    return enemy


if __name__ == "__main__":
    print(enemy_encounter(5))
Player.attack()
