"""Room class

>>> kwargs = {
...     'description': 'i am a room',
...     'contents': None,
...     'door_north': None,
...     'door_south': None,
...     'door_east': None,
...     'door_west': None,
...     'adjacent_north': None,
...     'adjacent_south': None,
...     'adjacent_east': None,
...     'adjacent_west': None
... }
>>> room = Room(**kwargs)
>>> room.description
'i am a room'

>>> room.contents is None
True

>>> room.door_north is None
True

>>> room.adjacent_north is None
True

"""

"""

State:
    description: <string>
    contents: (None, <pointer to an object>)
    door_north: (None, secret, locked, closed, open)
    door_south
    door_east
    door_west
    adjacent_north: (None, <pointer to another room>)
    adjacent_south
    adjacent_east
    adjacent_west

"""


class Room:
    """Blueprint for a room in the Dungeon of Doom!"""

    def __init__(self, **kwargs):
        """Initialize"""

        self.description = kwargs['description']
        self.contents = kwargs['contents']
        self.door_north = kwargs['door_north']
        self.door_south = kwargs['door_south']
        self.door_east = kwargs['door_east']
        self.door_west = kwargs['door_west']
        self.adjacent_north = kwargs['adjacent_north']
        self.adjacent_south = kwargs['adjacent_south']
        self.adjacent_east = kwargs['adjacent_east']
        self.adjacent_west = kwargs['adjacent_west']

    def __str__(self):
        return """Room(description={self.description}, contents={self.contents}, door_north={self.door_north},
            door_south={self.door_south}, door_east={self.door_east}, door_west={self.door_west})""".format(self=self)

    def __repr__(self):
        return """Room(description={self.description}, contents={self.contents}, door_north={self.door_north},
            door_south={self.door_south}, door_east={self.door_east}, door_west={self.door_west}),
            adjacent_north={self.adjacent_north}, adjacent_south={self.adjacent_south},
            adjacent_east={self.adjacent_east}, adjacent_west={self.adjacent_west}""".format(self=self)

    def has_thing(self, thing):
        """Return True or False for whether the contains the thing."""
        # thing can be any of the following: 'key', 'ring', 'dagger', 'treasure', 'spider'
        return self.contents and self.contents.i_am_a == thing

    def door_for_direction(self, direction):
        """Return the door for the direction given."""

        if direction == 'north':
            return self.door_north
        elif direction == 'south':
            return self.door_south
        elif direction == 'east':
            return self.door_east
        else:  # direction = 'west'
            return self.door_west

    def unlock_door_for_direction(self, direction):
        """Unlock the door for the direction given."""

        if direction == 'north':
            self.door_north = 'closed'
        elif direction == 'south':
            self.door_south = 'closed'
        elif direction == 'east':
            self.door_east = 'closed'
        else:  # direction = 'west'
            self.door_west = 'closed'

    def open_door_for_direction(self, direction):
        """Unlock the door for the direction given."""

        if direction == 'north':
            self.door_north = 'open'
        elif direction == 'south':
            self.door_south = 'open'
        elif direction == 'east':
            self.door_east = 'open'
        elif direction == 'west':
            self.door_west = 'open'

    def description_for_direction(self, direction):
        """Return the description that fits for the direction given."""

        door = self.door_for_direction(direction)

        if door == 'closed' or door == 'locked':
            return 'You are looking at a closed door.'
        elif door == 'open':
            return 'You are looking at an open door.'
        else:
            return 'You are looking at a wall.'

    def description_for_contents(self):
        """Return a description of the room’s contents."""

        if self.contents is not None:
            return 'You see {description}. {emoji}'.format(description=self.contents.description,
                                                           emoji=self.contents.emoji)
        else:
            return 'You see nothing of interest in this room.'

if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option
