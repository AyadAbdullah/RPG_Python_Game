from map import map_description


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
