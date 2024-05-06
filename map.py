#Map Module
from tabulate import tabulate

#File for map output
map_file = 'map.txt' 

def print_map(map_layout):
    """Prints the map layout as a table"""
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


