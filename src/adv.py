from room import Room
from player import Player
from item import Item

from colorama import Fore, Style, Back

# Declare all the items and rooms

sword = Item('sword', 'Pointy Stabby Guy')
potion = Item('potion', 'Alas it\'s just a flesh wound, but this might heal you?')
boom_bow = Item('boom_bow', 'Shoot your non-existant enemies from afar')
spike_trap = Item('spike_trap', 'Place on the wall to protect yourself')
clint = Item('clint', 'For help in manaje-ing your way around the rooms')
nick = Item('nick', 'Use your nick to debug your shitty code')
treasure = Item('treasure', '100 V-Bucks')

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [sword, clint, nick]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [potion]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [spike_trap]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [boom_bow]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [treasure]),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

current_room = room['outside']
player = Player(current_room)

# Write a loop that:
while True:
    print('\n')
# * Prints the current room name
    print(Fore.CYAN + player.location.name + '\n' + Style.RESET_ALL + '\n' + 'ITEMS IN ROOM')
    player.location.show_items()
    print(Style.RESET_ALL)
# * Prints the current description (the textwrap module might be useful here).
    print(Fore.BLACK + Back.WHITE + player.location.description + Style.RESET_ALL + '\n')
# * Waits for user input and decides what to do.
    user_input = input(Fore.YELLOW + "What should you do?\n [n] North [s] South [e] East [w] West [q] Quit \n [i] Inventory [g (name)] Get Item [d (name)] Drop Item \n ")
    # if user input is a one word command, these are the following actions
    if len(user_input.split(' ')) == 1:
    # If the user enters "q", quit the game.
        if user_input == 'q':
            break
        # If the user enters a cardinal direction, attempt  to move to the room there.
        elif user_input in ['n', 's', 'e', 'w']:
            if user_input == 'n':
                if player.location.n_to != None:
                    player.location = player.location.n_to
                else:
                    print('\n' + Fore.RED + 'You cannot move North from {}'.format(player.location.name))
            if user_input == 's':
                if player.location.s_to != None:
                    player.location = player.location.s_to
                else:
                    print('\n' + Fore.RED + 'You cannot move South from {}'.format(player.location.name))
            if user_input == 'e':
                if player.location.e_to != None:
                    player.location = player.location.e_to
                else:
                    print('\n' + Fore.RED + 'You cannot move East from {}'.format(player.location.name))
            if user_input == 'w':
                if player.location.w_to != None:
                    player.location = player.location.w_to
                else:
                    print('\n' + Fore.RED + 'You cannot move West from {}'.format(player.location.name))
        elif user_input == 'i':
            print('\n')
            player.show_inventory()
    # Print an error message if the movement isn't allowed.
        else:
            print(Fore.RED + '\nUnknown command:  Please try again!')
    elif len(user_input.split(' ')) == 2:
        first_input = user_input.split(' ')[0]
        second_input = user_input.split(' ')[1]
        # if user input g for get item command
        if first_input == 'g':
            if second_input in [i.name for i in player.location.items]:
                found = None
                for i in player.location.items:
                    if i.name == second_input:
                        found = i
                player.pick_up(found)
                player.location.remove_item(found)
            else:
                print(Fore.RED + "\nItem '{}' is not in {}".format(second_input, player.location.name))
        elif first_input == 'd':
            if second_input in [i.name for i in player.items]:
                found = None
                for i in player.items:
                    if i.name == second_input:
                        found = i
                player.drop(found)
                player.location.receive_item(found)
            else:
                print(Fore.RED + "\nItem '{}' is not in your inventory".format(second_input))


