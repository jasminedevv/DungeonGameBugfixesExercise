"""Game loop"""

import time
from player import Player
from room import Room
from key import Key
from dagger import Dagger
from spider import Spider
from treasure import Treasure

"""
State:
    game_state: underway|victory|defeat
    emoji: 🏰
    current_room: <pointer to a room instance>
    player: <pointer to the player instance>

Game play:
    welcome user to the game
    set up rooms
    create player
        prompt for name
        prompt for emoji
        show user list of possible actions (i.e. display help)
    display description of current (first) room
    prompt user to take an action
    each action is one iteration of the game loop
        on loop:
            check player health
            if player has the treasure, set game_state to 'victory', display victory message
            if player health is 'dead', set game_state to 'defeat', display defeat message
            if player health is 'alive'
                if game_state is 'underway', prompt for action, display description of current room

Room layout:
         ------
         | 12 |
    -----------
    | 21 | 22 |
    ----------------
    | 31 | 32 | 33 |
    ----------------

Parameters for each room:
    contents: (None, <pointer to an object>)
    door_north: (None, secret, locked, closed, open)
    door_south
    door_east
    door_west
    description: <string>

Properties added to each room after initialization:
    adjacent_north: (None, <pointer to another room>)
    adjacent_south
    adjacent_east
    adjacent_west
"""


def welcome_message():
    print('')
    print('--------------------------------------------------------------------------------')
    print('')
    print('Welcome to the Dungeon of Doom! Don’t even try to escape! 🏰')
    time.sleep(1)  # add a little drama...
    print('Your objective is to find the treasure. (Good luck with that!)')
    time.sleep(1)  # add a little drama...
    print('')
    print("Or die trying....")
    print('')
    time.sleep(1)  # add a little drama...


def rooms_setup():
    """Create the rooms (and their contents) in the Dungeon of Doom! Return the current room."""

    key = Key(description='a shiny, gold key')
    dagger = Dagger(description='a dagger, made of steel')
    spider = Spider(description='an extremely large, very hairy, very angry spider')
    treasure = Treasure(description='a large chest filled with treasure beyond your wildest imagination')

    # print(repr(key))
    # print(repr(dagger))
    # print(repr(spider))
    # print(repr(treasure))

    # create rooms (12 means row 1, column 2; 21 means row 2, column 1; and, so on...)
    # doors are set to open if the player would have had to pass through it from the other side
    room_12 = Room(contents=treasure, door_north=None, door_south='open', door_east=None, door_west=None,
                   description='You are in a circular room with gold leaf walls and a marble floor.',
                   adjacent_north=None, adjacent_south=None, adjacent_east=None, adjacent_west=None)
    room_21 = Room(contents=key, door_north=None, door_south=None, door_east='open', door_west=None,
                   description='You are in a small, non-descript room.\nThe only door is the one in through which you came.',
                   adjacent_north=None, adjacent_south=None, adjacent_east=None, adjacent_west=None)
    room_22 = Room(contents=spider, door_north='locked', door_south='open', door_east=None, door_west='closed',
                   description='You are in a large room with high ceilings.\nThere are doors to the North, West, and South.',
                   adjacent_north=None, adjacent_south=None, adjacent_east=None, adjacent_west=None)
    room_31 = Room(contents=None, door_north=None, door_south=None, door_east='open', door_west=None,
                   description='You are in an ornate bedroom.\nThe only door is the one in through which you came.',
                   adjacent_north=None, adjacent_south=None, adjacent_east=None, adjacent_west=None)
    room_32 = Room(contents=None, door_north='closed', door_south=None, door_east='closed', door_west='closed',
                   description='You are in a small, dank room with no windows and low ceilings.\nYou see doors to the West, North, and East.',
                   adjacent_north=None, adjacent_south=None, adjacent_east=None, adjacent_west=None)
    room_33 = Room(contents=dagger, door_north=None, door_south=None, door_east=None, door_west='open',
                   description='You are in a musty closet.\nThe only door is the one in through which you came.',
                   adjacent_north=None, adjacent_south=None, adjacent_east=None, adjacent_west=None)

    print(repr(room_32))

    # link rooms to each other (after initialization because we need refs to each room)
    room_12.adjacent_south = room_22

    room_21.adjacent_south = room_31
    room_21.adjacent_east = room_22

    room_22.adjacent_north = room_12
    room_22.adjacent_south = room_32
    room_22.adjacent_west = room_21

    room_31.adjacent_north = room_21
    room_31.adjacent_east = room_32

    room_32.adjacent_north = room_22
    room_32.adjacent_east = room_33
    room_32.adjacent_west = room_31

    room_33.adjacent_west = room_32

    print(repr(room_32))

    return room_32


def player_setup():
    """Set up the player, initialize the rooms and their contents."""
    print('--------------------------------------------------------------------------------')
    print('')
    print('What is your name? [Defaults to "Zelda"]')
    name = input()
    if not name:
        name = 'Zelda'
    print('Strange name, that. But, as you wish, {name}.'.format(name=name))
    print('')
    print('What is your symbol? [Defaults to 👸 ]')
    emoji = input()
    if not emoji:
        emoji = '👸'
    print('Fascinating. Kids today...')
    print('')
    player = Player(name, emoji)
    print('I dub thee, {description}'.format(description=player.description))
    print('Onwards!')
    print('')

    time.sleep(1)  # add a little drama...
    return player


def current_state(current_room, player):
    print('--------------------------------------------------------------------------------')
    print('')
    print(current_room.description)
    print(current_room.description_for_contents())
    print('You are facing {direction}.'.format(direction=player.direction.capitalize()))
    print(current_room.description_for_direction(player.direction))
    print('')
    time.sleep(1)  # add a little drama...


def end_game(player, game_state='underway'):
    if game_state == 'underway':  # player chose to exit the game
        print('Your loss! (Get it? Your loss because, by quitting the game early, you lost....)')
    elif game_state == 'victory':
        print('Congratulations! You won! You are now {name}, Slayer of Spiders! {emoji}'.format(name=player.name,
                                                                                                emoji=player.emoji))
    else:
        print('On noes! You died! So sorry for your luck.')
    print('Goodbye!')
    print('')
    time.sleep(1)  # add a little drama...


def main():
    game_state = 'underway'  # ('underway', 'victory', 'defeat')

    welcome_message()
    current_room = rooms_setup()
    player = player_setup()
    player.handle_action(current_room, 'h')
    player.handle_action(current_room, 'st')

    # print(repr(player))

    # game loop
    while game_state == 'underway':
        # check whether the game is over
        if player.has_thing('treasure'):
            game_state = 'victory'
        elif player.health == 'dead':
            game_state = 'defeat'
        else:
            # continue
            print('What are you going to do?')
            action = input()
            if action == 'q':  # quit the game by breaking out of the game loop
                break
            current_room = player.handle_action(current_room, action)
            current_state(current_room, player)

    end_game(player, game_state)

if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option
    main()
