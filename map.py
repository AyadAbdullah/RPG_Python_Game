#Map Module
from tabulate import tabulate

#File for map output
map_file = 'map.txt' 

def print_map(map_layout):
    """Prints the map layout as a table"""
    map_layout = list(map_layout)
    try:
        with open(map_file, "w") as file:
            file.write(tabulate(map_layout, tablefmt="fancy_grid"))
    except IOError:
        print("Unable to export map layout")
    finally:
        print("Maybe this will come in handy")


def ViewMap(map_layout, map_file):
    map_table_data = [[map_layout.get((row, col), "") 
                      for col in range(4)
                        for row in range(3)]]
    map_table = tabulate(map_table_data,tablefmt="fancy_grid")
    try:
        with open(map_file, "w") as file:
            file.write(map_table)
    except IOError:
        print("Error: Unable to write to file")
    finally:
        print("Maybe this will come in handy")
