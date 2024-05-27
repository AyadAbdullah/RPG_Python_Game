#######################################################################################
#Title: Hitman 2 Text Based Game Map
#Name:Ayad
#Class: CS30
#Assignment: Data Structures: RPG - Map
#Version: V3
#######################################################################################
"""
 The following code is based on the game Hitman 2, specifically 
 the The Finish Line mission.
"""
#######################################################################################

#IMPORTS AND GLOBAL VARIABLES-----------------------------------------------------------

from Interact import Interact
from Inventory import Inventory
from map import Map, map_description, map_table

#Room description and interactables

targets = 0

game_map = Map(map_table)
game_map.print_map()
game_inventory = Inventory()
game_interact = Interact()


current_position = (0, 0)
max_x = len(map_table) - 1  #Player positions
max_y = len(map_table[0]) - 1  #Player Positions

#FUNCTIONS------------------------------------------------------------------------------    
class Move:
    def __init__(self):
        pass
    def display_room_info(self, current_position):
        """
        This function will show the user the interactables and description of the room
        they enter.
        """
        if current_position in map_description:
            room_info = map_description[current_position]
            interactables = room_info.get("interactables", [])[:]
    
            print(room_info["description"])
            print("Interactables:", interactables)
    
    
    def display_room_description(self, current_position):
        """
        This function describes the room description based on the current position.
        """
        if current_position in map_description:
            print(map_description[current_position]["description"])
    
    
    def move(self, current_position, direction, max_x, max_y):
        """
        This function controls the movement of the player. Also makes sure
        that the user doesn't move outside the boundaries of the map.
        """
        x, y = current_position
        if direction == "north" and x > 0:
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
class Player(Inventory, Interact, Move):
    def __init__(self):
        super().__init__()

game_move = Move()

def user_message():
    "Just a user message that tells user what to do."
    print("Hello user, this is just a tutorial message.")
    print("The following are just some guidelines for you.")
    print("1. You can move with typing the direction you want to move in")
    print("2. In order to do anything other than moving" +
          " you can type the \ncoressponding number to do that action.")
    print("3. Just as a heads up some of the interactables are very long" +
          " which you can shorten the interactable name.")
    print("Lastly, It is recommended that you extend the console tab to" +
          " view the map properly(due to large names")
    print("Thanks for reading, hope you enjoy. \n\n\n\n")



def start_game():
    """
    This function starts the game.
    """

    global current_position, game_move
    user_message()
    print("Welcome to Hitman 2: The Text Adventure!")
    print("You are Agent 47, a highly skilled assasin")
    print("Your mission is to eliminate 2 targets, Robert and Sierra Knox")
    print("Be cautious and plan your moves carefully")

    while True:
        game_move.display_room_info(current_position)
        print("What do you want to do?")
        print("1. Move")
        print("2. View Map")
        print("3. Inventory")
        print("4. Interact")
        print("5. Quit")
        choice = input().lower()
        if choice == "1":
            print(
                "Which direction do you want to move?(north, south, east, west)"
            )
            action = input().lower()
            current_position = game_move.move(current_position, action, max_x, max_y)
        elif choice == "2":
            game_map.view_map()
        elif choice == "3":
            game_interact.inventory.view_inventory()
        elif choice == "4":
            game_interact.interact(current_position)
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Please select correct key to do the desired action")


#MAIN------------------------------------------------------------------------------------
if __name__ == "__main__":
    start_game()
