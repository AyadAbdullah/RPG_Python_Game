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

map_table = [[
    "Hawke's Bay", "Hawke's Bay Beach", "Miami Beach", "Security Room"
],
             [
                 "Hawke's Bay Safe House", "City Center", "Hotel & Expo Room",
                 "Kronstadt Industries"
             ],
             [
                 "Marquez Family Mansion", "VIP Area", "The Finish Line",
                 "Android Soldier Room"
             ]]

inventory = []

map_description = {
    (0, 0): {
        "description": "You have entered Hawke's Bay",
        "interactables": ["Beach Chair", "Surfboard"],
    },
    (0, 1): {
        "description": "You have entered at Hawke's Bay Beach",
        "interactables": ["Fishing Rod", "Shovel"]
    },
    (0, 2): {
        "description": "You are now at Miami Beach",
        "interactables": ["Beach Ball", "Beach Umbrella"],
    },
    (0, 3): {
        "description":
        "You entered the security room(The guards, inside, are confused",
        "interactables": ["Security Camera", "Keycard"],
    },
    (1, 0): {
        "description": "You are in the Hawke's Bay Safe House",
        "interactables": ["Safe", "Computer"],
    },
    (1, 1): {
        "description": "You have now entered the busy City Center",
        "interactables": ["Crowd", "Street Vendor"],
    },
    (1, 2): {
        "description":
        "You can choose to rest in the Hotel & Expo(obviously not in" +
        "the expo)",
        "interactables": ["Rest", "Explore"],
    },
    (1, 3): {
        "description":
        "You have now entered the high-tech Kronstadt Building." +
        " A robot greets you as you enter.",
        "interactables": ["Wrench", "Hammer"],
    },
    (2, 0): {
        "description": "You are now in the Marquez Family Mansion",
        "interactables": ["Guard", "Ted Mendez"],
    },
    (2, 1): {
        "description":
        "Want to relax? Well you're in the right place, The V.I.P Area.",
        "interactables":
        ["Bar", "Watch the Race", "Poison Sierra Knox's Drink"],
    },
    (2, 2): {
        "description":
        "You are now in the The Finish Line. You see a car with suspicious" +
        " enhancements",
        "interactables": ["Racing Car", "Screwdriver"],
    },
    (2, 3): {
        "description": "You entered the Android Soldier Testing room." +
        "There you see your target Robert Knox",
        "interactables": ["Robert Knox"],
    }
}

targets = 0
poisoned_drink = False
racing_car_sabotaged = False

max_x = len(map_table) - 1  #Player positions
max_y = len(map_table[0]) - 1  #Player Positions

m.print_map(map_table
            )  #Passing the above list to the map.py for exporting and tabulate
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


def add_to_inventory(item):
    """
    Add items to the user's inventory
    """
    inventory.append(item)
    print(f"{item} has been added to the inventory.")


def view_inventory():
    """
    Will help the user view inventory.
    """
    if inventory:
        print("Inventory: ")
        for item in inventory:
            print("-", item)
    else:
        print("Inventory is empty")


def increment_targets():
    """
    This functions add 1 to the global variable target, to 
    ensure if the mission has been complete or not.
    """
    global targets
    targets += 1


def check_killed_targets():
    """
    This function checks if both the targets have been killed or not.
    """

    global targets
    if targets == 2:
        print("Mission Accomplished. Good Work.")
        return True
    return False


def extra_interactables(action1):
    """
    This function controls just the interactables that are not
    important. 
    """
    extra_list = [
        "Beach Chair",
    ]
    if action1 == "Beach Chair":
        print("hahaha")
    elif action1 == "Surfboard":
        print("yes")
    elif action1 == "Fishing Rod":
        print("Heheheheh")
    elif action1 == "Shovel":
        print("no")
    elif action1 == "Beach Ball":
        print("heeh")
    elif action1 == "Beach Umbrella":
        print("nothing")
    elif action1 == "Crowd":
        print("gg")
    elif action1 == "Street Vendor":
        print("stop yellowlining")
    elif action1 == "Rest":
        print("Chelsea BTW")
    elif action1 == "Explore":
        print("fs in the chat")
    elif action1 == "Bar":
        print("hello world")
    else:
        print("Not a valid interactable object")


def actual_interact(action2):
    global poisoned_drink, racing_car_sabotaged
    actual_list = []
    if action2 == "Security Camera".lower:
        print("u")
    elif action2 == "Keycard".lower:
        print("k")
    elif action2 == "Safe".lower:
        print("h")
    elif action2 == "Computer".lower:
        print("j")
    elif action2 == "Wrench".lower:
        print("l")
    elif action2 == "Hammer".lower:
        print("U")
    elif action2 == "Poison Drink" or action2 == "Poison Sierra Knox's Drink".lower:
        print("t")
        poisoned_drink = True
    elif action2 == "Watch Race".lower:
        print("True or False")
    elif action2 == "Screwdriver".lower:
        print("gg")
    elif action2 == "Racing Car".lower:
        print("Give options")
        #elif racing car sabotaged = True
    elif action2 == "Guard".lower:
        print("y")


def interact():
    user_interact = input(
        "Which objects/character would you like to interact?")
    extra_interactables(user_interact)
    actual_interact(user_interact)


def general_interact_character(character):
    """
    This function will control what happens when the user
    interacts with differents characters/targets.
    """
    global targets

    if character == "Ted Mendez":
        print("As you explore you see Ted Mendez.")
        print("He is an arms dealer with connections to the targets")
        print("What do you want to do?")
        print("1. Kill him and take his disguise")
        print("2. Leave him alone")

        choice2 = int(input("Enter your choice(1 or 2):"))
        if choice2 == 1:
            print(
                "You distract Ted Mendez to a corner, where there is leaf shredder."
            )
            print(
                "You knock him out, take his disguise and dispose his body in the"
                + " leaf shredder.")
            add_to_inventory("Ted Mendez Disguise")
        elif choice2 == 2:
            print("You leave him alone.")
        else:
            print("Invalid Entry, try again")
    elif character == "Robert Knox":
        if "Ted Mendez Disguise" and "Robert Knox Picture" in inventory:
            print("You see your target Robert Knox")
            print("He gives you a demo of how the new generation of Android" +
                  " Soldiers shoot the target when shown their picture.")
            print(
                "He then asks you to try and you remember you found a picture of him"
                + "when you hacked the computer")
            print(
                "You give the picture to the Android Soldier and it identifies"
                + " him as target and shoots him to oblivion.")
            print("Good work, you killed one of your targets.")
            increment_targets()
            check_killed_targets()
        elif "Guard Disguise" in inventory:
            print("You escort Robert Knox to safe room as a safetly protocol.")
            print("Then you get him to isolate there")
            print(
                "You then proceed to assassinate him and dispose of the body.")
            print("Good work, you killed one of your targets.")
            increment_targets()
            check_killed_targets()
        else:
            print("You get caught without having a disguise.")
            print("Mission Failed.☹️")
            exit()

    elif character == "Sierra Knox":
        if "Guard Disguise" in inventory:
            print("You escort Robert Knox to safe room as a safetly protocol.")
            print("Then you get him to isolate there")
            print(
                "You then proceed to assassinate him and dispose of the body.")
            print("Good work, you killed one of your targets.")
            increment_targets()
            check_killed_targets()

        elif poisoned_drink is True:
            print(
                "Sierra Knox drinks the poisoned drink that you poisoned earlier"
            )
            print("Good work, you kill one of your targets")
            increment_targets()
            check_killed_targets()


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

    global current_position
    user_message()
    print("Welcome to Hitman 2: The Text Adventure!")
    print("You are Agent 47, a highly skilled assasin")
    print("Your mission is to eliminate 2 targets, Robert and Sierra Knox")
    print("Be cautious and plan your moves carefully")

    while True:
        display_room_info(current_position)
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
            current_position = move(current_position, action, max_x, max_y)
        elif choice == "2":
            print(tabulate(map_table, tablefmt="grid"))
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            pass
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Please '1' to move or '2' to quit")


#MAIN------------------------------------------------------------------------------------
if __name__ == "__main__":
    start_game()
