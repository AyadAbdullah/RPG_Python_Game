current_position = (0,0)

rooms = {
    (0,0):{"description":"Miami - Hawke's Bay,New Zealand"},
    (1,0):{"description":"Hawke's Bay Safe House"},
    (1,1):{"description":"Hawke's Bay Beach"},
    (2,0):{"description":"Miami-The Finish Line"},
    (3,0):{"description":"Miami - Miami Beach"},
    (3,1):{"description":"Miami - Kronstadt Industries"},
    (4,0):{"description":"Miami - City Center"},
    (4,1):{"description":"Miami - Marquez Family Mansion"},
}

def display_room_description(current_position):
    room = rooms[current_position]
    print("You are in: ", room["description"])

def move(current_position, direction):
    x,y = current_position
    if direction == "north" and (x - 1,y) in rooms:
        current_position = (x-1,y)
    elif direction == "south" and (x + 1,y) in rooms:
        current_position = (x+1,y)
    elif direction == "west" and (x,y-1) in rooms:
        current_position = (x, y - 1)
    elif direction == "east" and (x,y+1) in rooms:
        current_position = (x, y+1)
    else:
        print("You cannot move in that direction")
        return current_position

def start_game():
    global current_position 

    print("Welcome to Hitman 2: The Text Adventure!")
    print("You are Agent 47, a highly skilled assasin")
    print("Your mission is to eliminate your targets without getting caught")
    print("Be cautios and plan your moves carefully")
    while True:
        display_room_description(current_position)
        print("Which direction do you want to move?(north/south/east/west or q to quit)")
        action = input().lower
        if action == 'q':
            print("Thanks for playing!")
            break
        elif action in ["north","south","east","west"]:
            current_position = move(current_position, action)
        else:
            print("Invalid action. Please choose a valid direction or 'q' to quit")

if __name__ == "__main__":
    start_game()


    