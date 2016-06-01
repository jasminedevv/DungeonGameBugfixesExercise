"""Spider bad-guy class

>>> spider = Spider('i am a spider')
>>> spider.description
'i am a spider'

>>> spider.i_am_a
'spider'

"""

import re
import time
from animal import Animal

"""

State:
    emoji: 🕷
    ability: kill players
    health: alive|dead

"""


class Spider(Animal):
    """Blueprint for a spider in the Dungeon of Doom!

    Extends Animal
    """

    def __init__(self, description):
        """Initialize"""
        i_am_a = 'spider'
        emoji = '🕷'
        super().__init__(i_am_a, description, emoji)

    def __repr__(self):
        return """Spider(description={self.description}, i_am_a={self.i_am_a}""".format(self=self)

    def update_description(self):
        self.description = re.sub(r'angry|wounded', self.health, self.description)

    def attack(self, player):
        """Attack the player!"""
        if player.health == 'alive':
            player.health = 'wounded'
            print('The spider wounded you! {emoji}'.format(emoji=self.emoji))
            print('')
            time.sleep(1)  # add a little drama...
        elif player.health == 'wounded':
            player.health = 'dead'
            print('The spider killed you! {emoji}'.format(emoji=self.emoji))
            print('')
            time.sleep(1)  # add a little drama...

if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option
