"""Generic living thing class

>>> animal = Animal('animal', 'i am an animal')
>>> animal.description
'i am an animal'

>>> animal.i_am_a
'animal'

"""

import time

"""

State:
    description: <string>

"""


class Animal:
    """Blueprint for a generic living thing in the Dungeon of Doom!"""

    def __init__(self, i_am_a='animal', description=None, emoji=None):
        """Initialize"""
        self.health = 'alive'
        self.i_am_a = i_am_a
        self.description = description
        self.emoji = emoji

    def __repr__(self):
        return """Animal(description={self.description}, i_am_a={self.i_am_a}, emoji={self.emoji}""".format(self=self)

    def i_am_alive(self):
        return self.health == 'alive'

    def wound(self):
        self.health = 'wounded'
        print('The {i_am_a} has been wounded!'.format(i_am_a=self.i_am_a))
        print('')
        time.sleep(1)  # add a little drama...

    def kill(self):
        self.health = 'dead'
        print('The {i_am_a} has been killed!'.format(i_am_a=self.i_am_a))
        print('')
        time.sleep(1)  # add a little drama...

if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option
