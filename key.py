"""Key class, inherits from GenericObject

>>> key = Key('i am a key')
>>> key.description
'i am a key'

>>> key.i_am_a
'key'

"""

from genericobject import GenericObject

"""

State:
    emoji: 🔑
    ability: open locked doors

"""


class Key(GenericObject):
    """Blueprint for a key in the Dungeon of Doom!

    Extends GenericObject
    """

    def __init__(self, description):
        """Initialize"""
        super().__init__(description)
        self.i_am_a = 'key'
        self.emoji = '🔑'

    def __repr__(self):
        return """Key(description={self.description}, i_am_a={self.i_am_a}, emoji={self.emoji}""".format(self=self)

if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option
