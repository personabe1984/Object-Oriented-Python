# from monster import Monster
import random

from combat import Combat

COLOR = ['yellow', 'red', 'blue', 'green']


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    hit_points = 1
    weapon = 'sword'
    color = 'yellow'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLOR)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.experience)

    def battlecry(self):
        return self.sound.upper()


# Subclass
class Goblin(Monster):
    max_hit_points = 3
    max_experience = 2
    sound = 'squeak'


class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = 'growl'


class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = 'raaaaaaar'



jubjub = Monster()
jubjub.battlecry()


jabberwock = Monster(color='blue', sound='whiffling', hit_points=500, adjective='manxsome')


"""
        self.hit_points = kwargs.get('hit_points', 1)
        self.weapon = kwargs.get('weapon', 'sword')
        self.color = kwargs.get('color', 'yellow')
        self.sound = kwargs.get('sound', 'roar')

"""