#######################################################################################
#Title: Hitman 2 Text Based Game Map
#Name:Ayad
#Class: CS30
#Assignment: Data Structures: RPG - Map
#Version: V2.1(Actually 2.0)
#######################################################################################
"""
 The following code is based on the game Hitman 2, specifically 
 the The Finish Line missing.
"""
#######################################################################################

#IMPORTS AND GLOBAL VARIABLES-----------------------------------------------------------
import map as m

current_position = (0, 0)

map_table = [["Hawke's Bay", "Hawke's Bay Beach", "Miami Beach", "Security Room"],
    ["Hawke's Bay Safe House","City Center","Hotel & Expo Room","Kronstadt Industries"],
    ["Marquez Family Mansion","VIP Area","The Finish Line", "Android Soldier Room"]
]

max_x = len(map_table) - 1
max_y = len(map_table[0]) - 1

m.print_map(map_table) #Passing the above list to the map.py for exporting and tabulate
m.ViewMap('map.txt')

#FUNCTIONS------------------------------------------------------------------------------
def display_room_description(current_position):
    """
    This function displays the room description based on the current position.
    """
    x, y = current_position
    room_description = map_table[x][y]
    print("You are in: ", room_description)


def move(current_position, direction, max_x, max_y):
    """
    This function controls the movement of the player. Also makes sure
    that the user doesn't move outside the boundaries of the map.
    """
    x, y = current_position
    if direction == "north" and x>0:
        current_position = (x - 1, y)
    elif direction == "south" and x < max_x:
        current_position = (x + 1, y)
    elif direction == "west" and y > 0:
        current_position = (x, y - 1)
    elif direction == "east" and y < max_y:
        current_position = (x, y + 1)
    else:
        print("You cannot move in that direction")
    return current_position


def start_game():
    """
    This function starts the game.
    """

    global current_position

    print("Welcome to Hitman 2: The Text Adventure!")
    print("You are Agent 47, a highly skilled assasin")
    print("Your mission is to eliminate your targets without getting caught")
    print("Be cautious and plan your moves carefully")

    while True:
        display_room_description(current_position)
        print("What do you want to do?")
        print("1. Move")
        print("2. Quit")
        choice = input().lower()
        if choice == "1":
            print("Which direction do you want to move?(north, south, east, west)")
            action = input().lower()
            current_position = move(current_position, action, max_x, max_y)
        elif choice == "2":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Please '1' to move or '2' to quit")

#MAIN------------------------------------------------------------------------------------
if __name__ == "__main__":
    start_game()
