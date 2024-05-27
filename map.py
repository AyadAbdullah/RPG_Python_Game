#Map Module
from tabulate import tabulate

map_file = 'map.txt'

current_position = (0, 0)
map_table = [
     ["Hawke's Bay", "Hawke's Bay Beach", "Miami Beach", "Security Room"],
     ["Hawke's Bay Safe House", "City Center", "Hotel & Expo Room",
         "Kronstadt Industries"],
     ["Marquez Family Mansion", "VIP Area", "The Finish Line",
         "Android Soldier Room"]
    ]#Map List for Table


map_description = {
    (0, 0): {
    "description": "You have entered Hawke's Bay",
    },
    (0, 1): {
    "description": "You have entered at Hawke's Bay Beach",
    },
    (0, 2): {
    "description": "You are now at Miami Beach",
    },
    (0, 3): {
    "description":
    "You entered the security room(The guards, inside, are confused)",
    "interactables": ["Security Camera", "Keycard"],
    },
    (1, 0): {
    "description": "You are in the Hawke's Bay Safe House",
    "interactables": ["Safe", "Computer"],
    },
    (1, 1): {
    "description": "You have now entered the busy City Center",
    },
    (1, 2): {
    "description":
    "You arrive at the hotel, you see guests taking pictures and you see"+
    " the expo where lies the great inventions made by the Kronstadt Industries.",
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
    ["Watch the Race", "Poison Sierra Knox's Drink"],
    "conditional_interactable" : ["Sierra Knox"]
    },
    (2, 2): {
    "description":
    "You are now in the The Finish Line pit stop. You see a car with suspicious" +
    " enhancements",
    "interactables": ["Racing Car", "Screwdriver"],
    },
    (2, 3): {
    "description": "You entered the Android Soldier Testing room." +
    "There you see your target Robert Knox",
    "interactables": ["Robert Knox"],
    }
}


class Map:
    def __init__(self, map_layout, map_file='map.txt'):
        self.map_layout = map_layout
        self.map_file = map_file

    def print_map(self):
        """
        Prints the map layout as a table.
        """
        try:
            with open(self.map_file, "w") as file:
                file.write(tabulate(self.map_layout, tablefmt = "grid"))
        except IOError:
                    print("Unable to export map layout")

    def view_map(self):
        """
        Displays the map file content
        """
        try:
            with open(self.map_file, "r") as file:
                print(file.read())
        except IOError:
            print("Error: Unable to read the map file.")






