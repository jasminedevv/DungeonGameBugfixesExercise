"""Dagger class, inherits from GenericObject

>>> dagger = Dagger('i am a dagger')
>>> dagger.description
'i am a dagger'

>>> dagger.i_am_a
'dagger'

"""

from genericobject import GenericObject

"""

State:
    emoji: 🗡
    ability: kill spiders

"""


class Dagger(GenericObject):
    """Blueprint for a dagger in the Dungeon of Doom!

    Extends GenericObject
    """

    def __init__(self, description):
        """Initialize"""
        super().__init__(description)
        self.i_am_a = 'dagger'
        self.emoji = '🗡'

    def __repr__(self):
        return """Dagger(description={self.description}, i_am_a={self.i_am_a}, emoji={self.emoji}""".format(self=self)

if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option
