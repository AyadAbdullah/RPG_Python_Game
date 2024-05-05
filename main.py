#######################################################################################
#Title: Hitman 2 Text Based Game Map
#Name:Ayad
#Class: CS30
#Assignment: Data Structures: RPG - Map
#Version: V1
#######################################################################################
"""
 The following code is based on the game Hitman 2, specifically 
 the The Finish Line missing.
"""
#######################################################################################

#IMPORTS AND GLOBAL VARIABLES-----------------------------------------------------------
import map

current_position = (0, 0)

map_layout = {
    (0, 0): "Hawke's Bay, New Zealand",
    (0, 1): "Hawke's Bay Beach",
    (0, 2): "Miami Beach",
    (0, 3): "Security Room",
    (1, 0): "Hawke's Bay Safe House",
    (1, 1): "City Center",
    (1, 2): "Hotel & Expo Room",
    (1, 3): "Kronstadt Industries",
    (2, 0): "Marquez Family Mansion",
    (2, 1): "VIP Area",
    (2, 2): "The Finish Line",
    (2, 3): "Android Soldier Testing Room",
}
map.print_map(map_layout)
map.ViewMap(map_layout,'map.txt')

#FUNCTIONS------------------------------------------------------------------------------
def display_room_description(current_position):
    """
    This function displays the room description based on the current position.
    """
    room_description = map_layout[current_position]
    print("You are in: ", room_description)


def move(current_position, direction):
    """
    This function controls the movement of the player. Also makes sure
    that the user doesn't move outside the boundaries of the map.
    """
    x, y = current_position
    if direction == "north" and (x - 1, y) in map_layout:
        current_position = (x - 1, y)
    elif direction == "south" and (x + 1, y) in map_layout:
        current_position = (x + 1, y)
    elif direction == "west" and (x, y - 1) in map_layout:
        current_position = (x, y - 1)
    elif direction == "east" and (x, y + 1) in map_layout:
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
        if choice == "2":
            print("Thanks for playing!")
            break
        elif choice == "1":
            print("Which direction do you want to move?(north, south, east, west)")
            action = input().lower()
            current_position = move(current_position, action)
        else:
            print(
                "Invalid action. Please choose a valid direction or '2' to quit"
            )


#MAIN------------------------------------------------------------------------------------
if __name__ == "__main__":
    start_game()
