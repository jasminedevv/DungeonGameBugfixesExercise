"""Treasure class, inherits from GenericObject

>>> treasure = Treasure('i am treasure')
>>> treasure.description
'i am treasure'

>>> treasure.i_am_a
'treasure'

"""

from genericobject import GenericObject

"""

State:
    emoji: 💰
    ability: grant immeasurable wealth

"""


class Treasure(GenericObject):
    """Blueprint for the treasure in the Dungeon of Doom!

    Extends GenericObject
    """

    def __init__(self, description):
        """Initialize"""
        super().__init__(description)
        self.i_am_a = 'treasure'
        self.emoji = '💰'

    def __repr__(self):
        return """Treasure(description={self.description}, i_am_a={self.i_am_a}, emoji={self.emoji}""".format(self=self)

if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option
