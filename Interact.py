actual_interact_list = ["Security Camera", "Keycard", "Safe", "Computer", "Wrench",
      "Hammer", "Poison Drink", "Poison Sierra Knox's Drink",
      "Watch Race", "Screwdriver", "Racing Car", "Guard"]#for actual interact

extra_interact_list = ["Beach Chair", "Surfboard", "Fishing Rod", "Shovel", 
   "Beach Ball", "Beach Umbrella", "Crowd", "Street Vendor",
  "Rest", "Explore", "Bar"]#for extra interact

character_list = ["Ted Mendez", "Robert Knox", "Sierra Knox"]#For character interact


def extra_interactables(action1):
    """
    This function controls just the interactables that are not
    important. 
    """

    if action1 == "Beach Chair":
        print("You sit in the Beach chair and enjoy for a moment, before realising"+
             " you are here to kill.")

    elif action1 == "Surfboard":
        print("Oh come on! You gotta go kill you're targets.")
        remove_interactable(current_position, "Surfboard")
    elif action1 == "Fishing Rod":
        print("You go fishing and catch a fish.")
        add_to_inventory("Fish")
    elif action1 == "Shovel":
        add_to_inventory("Shovel")
        remove_interactable(current_position, "Shovel")
    elif action1 == "Beach Ball":
        print("Sorry, I know you want to have fun, but you are on an assination"+
             " mission, so don't mess around.")
        remove_interactable(current_position, "Beach Ball")
    elif action1 == "Beach Umbrella":
        print("You sit under the umbrella and get up immediately when a voice"+ 
              "whispers  '...targetsssss' ")
    elif action1 == "Crowd":
        print("You interact with the crowd and socialize? You then remember"+
             " you're here to assinate 2 people.")
    elif action1 == "Street Vendor":
        print("You bribe the street vendor and take all his money.")
    elif action1 == "Rest":
        print(" You book a hotel room and decide to rest in it.")
        print(" To the user: you probably should have known what will")
        print(" happen when you selected this.")
        exit()
    elif action1 == "Explore":
        print("You look at multiple inventions of the Kronstadt Industries")
    elif action1 == "Bar":
        print("You almost drank a shot but gladly restrained. Remember drinking is "+
              " haram.")
    else:
        print("Not a valid interactable object")


def actual_interact(action2):
    global poisoned_drink, racing_car_sabotaged


    if action2 == "Security Camera":
        print("You disable the camera")
    elif action2 == "Keycard":
        print("You find some idiot guard's lost keycard. You pick it up")
        add_to_inventory("Keycard")
        remove_interactable(current_position, "Keycard")
    elif action2 == "Safe":
        if "Keycard" in inventory:
            print("You open the safe with the keycard and find important documents.")
            remove_interactable(current_position, "Safe")
        else:
            print("You need a keycard to open the safe.")
    elif action2 == "Computer":
        print("You hack the computer and find a photo of Robert Knox."+
             "You print it out and keep it with you.")
        add_to_inventory("Robert Knox's picture")
    elif action2 == "Wrench":
        add_to_inventory("Wrench")
        remove_interactable(current_position, "Wrench")
    elif action2 == "Hammer":
        add_to_inventory("Hammer")
        remove_interactable(current_position, "Hammer")
    elif action2 == "Poison Drink" or action2 == "Poison Sierra Knox's Drink":
        print("You see a VIP table with a cup that says"+
             " 'Congrats Sierra for your win!',"+
             " knowing she is your target you poison the drink in secret.")
        poisoned_drink = True

    elif action2 == "Watch Race":
        if not racing_car_sabotaged:
            print("You watch the main spectacle of the venue.")
            print("When the racers names are called out you see Sierra Knox, one of"+
                  " your targets")
            print("You realise you could have sabotaged the car and killed her and"+
                 " made it look like an accident")
            print("Anyways there are more ways to kill. ( ͡❛ ͜ʖ ͡❛)✌")
        elif racing_car_sabotaged:
            print("You watch the main spectacle of the venue.")
            print("When the racers names are celled out you see Sierra Knox, one of"+
                  " your targets")
            print("You remember you sabotaged the racing car with the name Sierra Knox")
            print("You smile and wait for the fun to happen")
            print("As soon as the announcer says GO! nothing happens.")
            print("A few laps go by and all of a sudden you see Sierra Knox's car turning"
                 +" the corner and you see it loses control and crashes and explodes"
                 + " immediately. Good kill ( ͡❛ ͜ʖ ͡❛)👌")
            increment_targets()
        else:
            pass

    elif action2 == "Screwdriver":
        add_to_inventory("Screwdriver")
        remove_interactable(current_position, "Screwdriver")

    elif action2 == "Racing Car":
        print("As you decide to take a closer look at the car, you find it is none"
             + " other than Sierra Knox's, one of your targets?")
        sabotage = input("What do you want to do? sabotage or pass?").lower()

        if sabotage == "sabotage":
            print("You sabotaged the car, now you can wait and see what will happen"+
                 " when you watch the race.")
            racing_car_sabotaged = True
        else:
            print("( ͡❛  ͟ʖ ͡❛)")

    elif action2 == "Guard":
        weapons = ["Hammer", "Wrench", "Shovel", "Fish"] 
        available_weapons = [weapon for weapon in weapons if weapon in inventory]

        if available_weapons:
            print(f"You have {' , '.join(available_weapons)}")
            kill_action = input("Which one do you want to use to kill the guard?")

            if kill_action in available_weapons:
                print(f"You beat the guard with the {kill_action} and kill him"+ 
                      " and take his disguise.")
                add_to_inventory("Guard Disguise")
                remove_interactable(current_position, "Guard")
            else:
                print("You just punch him to death")
                add_to_inventory("Guard Disguise")
                remove_interactable(current_position, "Guard")
        else:
            print("You bring the guard to a corner and punch him to death.")
            add_to_inventory("Guard Disguise")
            remove_interactable(current_position, "Guard")

    else:
        print("Not a valid interactable object")

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
                "You then knock him out, take his disguise and dispose his body in the"
                + " leaf shredder.")
            add_to_inventory("Ted Mendez Disguise")
            remove_interactable(current_position, "Ted Mendez")
        elif choice2 == 2:
            print("You leave him alone.")
        else:
            print("Invalid Entry, try again")
    elif character == "Robert Knox":
        if "Ted Mendez Disguise" and "Robert Knox's picture" in inventory:
            print("You see your target Robert Knox")
            print("He recognizes you as Ted Mendez.")
            print("He gives you a demo of how the new generation of Android" +
                  " Soldiers that shoot their target when shown their picture.")
            print(
                "He then asks you to try and then you remember you" +
                " found a picture of him"
                + " when you hacked the computer")
            print(
                "You give the picture to the Android Soldier and it identifies"
                + " him as target and shoots him to oblivion.")
            print("Good work, you killed one of your targets.")
            increment_targets()
            check_killed_targets()
            remove_interactable(current_position, "Robert Knox")
        elif "Guard Disguise" in inventory:
            print("You escort Robert Knox to safe room as a safetly protocol.")
            print("Then you get him to isolate there")
            print(
                "You then proceed to assassinate him and dispose of the body.")
            print("Good work, you killed one of your targets.")
            increment_targets()
            check_killed_targets()
            remove_interactable(current_position, "Robert Knox")
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
            remove_interactable(current_position, "Sierra Knox")

        elif poisoned_drink:
            print(
                "Sierra Knox drinks the poisoned drink that you poisoned earlier")
            print("Good work, you kill one of your targets")
            increment_targets()
            check_killed_targets()
            remove_interactable(current_position, "Sierra Knox")

def interact():
    user_interact = input(
        "Which objects/character would you like to interact?")
    if user_interact in extra_interact_list:
        extra_interactables(user_interact)
    elif user_interact in actual_interact_list:
        actual_interact(user_interact)
    elif user_interact in character_list:
        general_interact_character(user_interact)


def remove_interactable(current_position1, interactable):
    """
    Remove an interactable object/character after interacted with
    """
    if current_position1 in map_description:
        room_info = map_description[current_position]
        if interactable in room_info["interactables"]:
            room_info["interactables"].remove(interactable)