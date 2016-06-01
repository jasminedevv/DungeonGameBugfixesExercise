"""Player class

>>> player = Player('Zelda', 'Z')
>>> player.description
'Zelda, Slayer of Pigeons! Z'

>>> player.i_am_a
'player'

"""

import time
from animal import Animal

"""

State:
    name: (prompt player to set at start of the game, default to Zelda)
    emoji: (prompt player to set at start of the game, default to 👸)
    health: alive|wounded|dead
    visibility: visible|invisible
    direction: north|south|east|west (defaults to north)
    possessions: []

Methods:
    help (display list of possible actions)
    status (display the player's name, health, and possessions)
    move (always forward)
    turn_left
    turn_right
    pick_up (requires object)
    unlock (requires key)
    open (requires door)
    attack (requires dagger)

"""


class Player(Animal):
    """The player in the Dungeon of Doom.

    Extends Animal
    """

    def __init__(self, name, emoji):
        description = name + ', Slayer of Pigeons! ' + emoji
        i_am_a = 'player'
        super().__init__(i_am_a, description, emoji)
        self.name = name
        self.visibility = 'visible'
        self.direction = 'north'
        self.possessions = []

    def __repr__(self):
        return """Player(description={self.description}, i_am_a={self.i_am_a}, name={self.name},
            visibility={self.visibility}, direction={self.direction},
            possessions={self.possessions}""".format(self=self)

    def handle_action(self, current_room, action='help'):
        """Do the specified action (default to showing the player their options).

        Moving is the only action that might change the current room.
        """
        previous_room = current_room  # used to decide whether to let the spider attack

        if action == 'm' or action == 'f':
            current_room = self.move(current_room)
        elif action == 'n':
            self.turn(current_room, 'north')
        elif action == 's':
            self.turn(current_room, 'south')
        elif action == 'e':
            self.turn(current_room, 'east')
        elif action == 'w':
            self.turn(current_room, 'west')
        elif action == 'pu':
            self.pick_up(current_room)
        elif action == 'u':
            self.unlock(current_room)
        elif action == 'o':
            self.open(current_room)
        elif action == 'a':
            self.attack(current_room)
        elif action == 'st' or action == 'i':
            self.status(current_room)
        else:  # default to showing the player what they can do
            self.help()

        # if we are not new to this room and the room has a spider, let it attack
        if previous_room == current_room and current_room.has_thing(
                'spider') and current_room.contents.health != 'dead':
            current_room.contents.attack(self)

        return current_room

    def help(self):
        """Print the possible commands for the player."""
        print('--------------------------------------------------------------------------------')
        print('')
        print('The following are the things you can do:')
        print('')
        print('f or m - Move (forward, always forward!)')
        print('n - Turn to face North')
        print('s - Turn to face South')
        print('e - Turn to face East')
        print('w - Turn to face West')
        print('pu - Pick up whatever is in the room')
        print('u - Unlock a door (requires a key)')
        print('o - Open the door in front of you (requires a door!)')
        print('a - Attack (requires something to attack)')
        print('st or i - Show your current status (inventory)')
        print('h - Dislpay this help text')
        print('q - Quit the game')  # unlike the other commands, this is handled in the game loop
        print('')
        print('To do one of the things, type the command, then press [enter].')
        print('')

    def status(self, current_room):
        """Print the current status of the player."""
        print('--------------------------------------------------------------------------------')
        print('')
        print('You are {description}'.format(description=self.description))
        print('You are {health}.'.format(health=self.health))
        if self.visibility == 'invisible':
            print('You are invisible!')
        if len(self.possessions) > 0:
            print('You possess the following items:')
            for p in self.possessions:
                print('• {description} {emoji}'.format(description=p.description.capitalize(), emoji=p.emoji))
        else:
            print('You have no possessions.')
        print('')
        time.sleep(1)  # add a little drama...

    def has_thing(self, thing):
        """Return True or False for whether the player is in possession of the thing."""
        # thing can only be one of the following: 'key', 'ring', 'dagger', 'treasure'
        for t in self.possessions:
            if thing == t.i_am_a:
                return True
        return False

    def turn(self, current_room, direction):
        """Turn player to face the direction passed in."""
        self.direction = direction

    def move(self, current_room):
        """Move the player (always forward)"""
        # if there is an open door in the direction the player is facing, then proceed
        # otherwise, inform the player of the obstacle (closed door or wall)

        msg_door_closed = 'You can’t walk through a closed door!'
        msg_wall = 'You can’t walk through a wall!'

        if self.direction == 'north':
            if current_room.door_north == 'closed' or current_room.door_north == 'locked':
                print(msg_door_closed)
            elif current_room.door_north == 'open':
                current_room = current_room.adjacent_north
            else:
                print(msg_wall)
        elif self.direction == 'south':
            if current_room.door_south == 'closed' or current_room.door_south == 'locked':
                print(msg_door_closed)
            elif current_room.door_south == 'open':
                current_room = current_room.adjacent_south
            else:
                print(msg_wall)
        elif self.direction == 'east':
            if current_room.door_east == 'closed' or current_room.door_east == 'locked':
                print(msg_door_closed)
            elif current_room.door_east == 'open':
                current_room = current_room.adjacent_east
            else:
                print(msg_wall)
        else:  # direction = 'west'
            if current_room.door_west == 'closed' or current_room.door_west == 'locked':
                print(msg_door_closed)
            elif current_room.door_west == 'open':
                current_room = current_room.adjacent_west
            else:
                print(msg_wall)

        time.sleep(1)  # add a little drama...
        return current_room

    def unlock(self, current_room):
        """Unlock the door in front of the player (requires key)"""

        has_key = self.has_thing('key')
        door = current_room.door_for_direction(self.direction)

        if door is None:
            print('You can’t open a wall!')
        elif door == 'locked':
            if has_key:
                current_room.unlock_door_for_direction(self.direction)
                print('You unlocked the door.')
            else:
                print('You can’t unlock a door without a key!')
        elif door == 'open':
            print('Um, the door was already open.')
        else:  # open the door
            print('Um, the door was already unlocked.')

        time.sleep(1)  # add a little drama...
        return current_room

    def open(self, current_room):
        """Open the door in front of the player (requires door)"""

        has_key = self.has_thing('key')
        door = current_room.door_for_direction(self.direction)

        if door is None:
            print('You can’t open a wall!')
        elif door == 'locked':
            if has_key:
                print('You must unlock the door before you can open it.')
            else:
                print('You can’t open a locked door without a key!')
        elif door == 'open':
            print('Um, the door was already open.')
        else:  # open the door
            current_room.open_door_for_direction(self.direction)

        time.sleep(1)  # add a little drama...
        return current_room

    def pick_up(self, current_room):
        """Pick up whatever is in the room (requires object)"""

        if current_room.contents is not None:
            print('You picked up {description}. {emoji}'.format(description=current_room.contents.description,
                                                                emoji=current_room.contents.emoji))
            # pick up the object
            self.possessions.append(current_room.contents)
            # remove the object from the room
            current_room.contents = None
        else:
            print('There is nothing here to pick up.')

        time.sleep(1)  # add a little drama...
        return current_room

    def attack(self, current_room):
        """Attack the spider (requires dagger)"""
        # if the room has a spider
        if current_room.has_thing('spider'):
            # let the player act
            if self.has_thing('dagger'):
                if current_room.contents.health == 'wounded':
                    """Kill the spider!"""
                    current_room.contents.kill()
                    current_room.contents.update_description()
                elif current_room.contents.health == 'wounded':
                    """Wound the spider"""
                    current_room.contents.wound()
                    current_room.contents.update_description()
                else:
                    print('OK, OK, it’s dead already!')
            else:
                print('You need a dagger to attack things.')
        # else: there is nothing to attack
        else:
            print('There is nothing to attack in this room.')

        time.sleep(1)  # add a little drama...
        return current_room

if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option
