"""Generic object class

>>> obj = GenericObject('i am an object')
>>> obj.description
'i am an object'

"""

"""

State:
    description: <string>

"""


class GenericObject:
    """Blueprint for a generic object in the Dungeon of Doom!"""

    def __init__(self, description):
        """Initialize"""
        self.description = description

    def __repr__(self):
        return """GenericObject(description={self.description}""".format(self=self)

if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option
