#######################################################################################
#Title: Hitman 2 Text Based Game Map
#Name:Ayad
#Class: CS30
#Assignment: Data Structures: RPG - Map
#Version: V3
#######################################################################################
"""
 The following code is based on the game Hitman 2, specifically 
 the The Finish Line missing.
"""
#######################################################################################

#IMPORTS AND GLOBAL VARIABLES-----------------------------------------------------------
from tabulate import tabulate

import map as m

current_position = (0, 0)

map_table = [["Hawke's Bay", "Hawke's Bay Beach", "Miami Beach", "Security Room"],
    ["Hawke's Bay Safe House","City Center","Hotel & Expo Room","Kronstadt Industries"],
    ["Marquez Family Mansion","VIP Area","The Finish Line", "Android Soldier Room"]
]
map_description = {
    (0, 0):{
    "description": "You have entered Hawke's Bay",
    "interactables":["Beach Chair", "Surfboard"],
    },
    (0, 1):{
    "description":"You have entered at Hawke's Bay Beach",
    "interactables":["Fishing Rod", "Shovel"]
    },
    (0, 2):{
    "description":"You are now at Miami Beach",
    "interactables":["Beach Ball", "Beach Umbrella"],
    },
    (0, 3):{
    "description":"You entered the security room(The guards, inside, are confused",
    "interactables":["Security Camera", "Keycard"],
    },
    
    (1, 0):{
    "description":"You are in the Hawke's Bay Safe House",
    "interactables":["Safe", "Computer"],
    },
    (1, 1):{
    "description":"You have now entered the busy City Center",
    "interactables":["Crowd", "Street Vendor"],
    },
    (1, 2):{
    "description":"You can choose to rest in the Hotel & Expo(obviously not in"+ 
    "the expo)",
    "interactables":["Rest", "Explore"],
    },
    (1, 3):{
    "description":"You have now entered the high-tech Kronstadt Building."+
    " A robot greets you as you enter.",
    "interactables":["Security Camera", "Keycard"],
    },
     
    (2, 0):{
    "description":"You are now in the Marquez Family Mansion",
    "interactables":["Guard","Lawn Mower","Ted Mendez"],
    },
    (2, 1):{
    "description":"Want to relax? Well you're in the right place, The V.I.P Area.",
    "interactables":["Bar","Watch the Race", "Poison Sierra Knox's Drink"],
    },
    (2, 2):{
    "description":"You are now in the The Finish Line. You see a car with suspicious"+
        " enhancements",
    "interactables":["Racing Car", "Screwdriver"],
   },
    (2, 3): {
    "description":"You entered the Android Soldier Testing room." + 
        "There you see your target Robert Knox",
    "interactables":["Robert Knox"],
   }
}
max_x = len(map_table) - 1 #Player positions
max_y = len(map_table[0]) - 1 #Player Positions

m.print_map(map_table) #Passing the above list to the map.py for exporting and tabulate
m.ViewMap('map.txt')

#FUNCTIONS------------------------------------------------------------------------------
def display_room_info(current_position):
    """
    This function will show the user the interactables and description of the room
    they enter.
    """
    if current_position in map_description:
        room_info = map_description[current_position] 
        print(room_info["description"])
        print("Interactables:", room_info["interactables"])


def display_room_description(current_position):
    """
    This function describes the room description based on the current position.
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

def user_message():
    "Just a user message that tells user what to do."
    print("Hello user, this is just a tutorial message.")
    print("The following are just some guidelines for you.")
    print("1. You can move with typing the direction you want to move in")
    print("2. In order to do anything other than moving" +
          " you can type the \ncoressponding number to do that action.")
    print("Lastly, it is recommended that you extend the console table to"+
         " view the map properly(due to large names")
    print("Thanks for reading, hope you enjoy. \n\n\n\n")

def start_game():
    """
    This function starts the game.
    """

    global current_position
    user_message()
    print("Welcome to Hitman 2: The Text Adventure!")
    print("You are Agent 47, a highly skilled assasin")
    print("Your mission is to eliminate your targets without getting caught")
    print("Be cautious and plan your moves carefully")

    while True:
        display_room_info(current_position)
        print("What do you want to do?")
        print("1. Move")
        print("2. View Map")
        print("3. Quit")
        choice = input().lower()
        if choice == "1":
            print("Which direction do you want to move?(north, south, east, west)")
            action = input().lower()
            current_position = move(current_position, action, max_x, max_y)
        elif choice == "2":
            print(tabulate(map_table, tablefmt = "grid"))
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Please '1' to move or '2' to quit")

#MAIN------------------------------------------------------------------------------------
if __name__ == "__main__":
    start_game()
