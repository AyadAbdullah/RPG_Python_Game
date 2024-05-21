#Map Module
from tabulate import tabulate

map_file = 'map.txt'

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






"""
#File for map output
map_file = 'map.txt' 

def print_map(map_layout):
    ""Prints the map layout as a table"
    try:
        with open(map_file, "w") as file:
            file.write(tabulate(map_layout, tablefmt = "grid"))
    except IOError:
        print("Unable to export map layout")
    finally:
        pass


def ViewMap(map_file):
    try:
        with open(map_file, "r") as file:
            file.read()
    except IOError:
        print("Error: Unable to write to file")
    finally:
        pass
"""

