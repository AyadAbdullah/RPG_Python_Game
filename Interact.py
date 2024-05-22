import Inventory as inv
import main


class Interact:
    def __inti__(self, inventory):
        """
        Intialize the invenotry class
        """
        self.inventory = inventory
        self.poisoned_drink = False
        self.racing_car_sabotaged = False
        self.actual_interact_list = [
            "Security Camera", "Keycard", "Safe", "Computer", "Wrench",
          "Hammer", "Poison Drink", "Poison Sierra Knox's Drink",
          "Watch Race", "Screwdriver", "Racing Car", "Guard"]
        #The above is for actual interactable actions that will help the 
        #user complete the task.
    
        self.character_list = ["Ted Mendez", "Robert Knox", "Sierra Knox"]
        #For character interact which allow the user to kill.
        
        
        def task_interact(self, action2):
            global poisoned_drink, racing_car_sabotaged
        
        
            if action2 == "Security Camera":
                print("You disable the camera")
            elif action2 == "Keycard":
                print("You find some idiot guard's lost keycard. You pick it up")
                self.add_to_inventory("Keycard")
                remove_interactable(main.current_position, "Keycard")
            elif action2 == "Fishing Rod":
                print("You go fishing and catch a fish.")
                self.add_to_inventory("Fish")
            elif action2 == "Safe":
                if "Keycard" in inventory:
                    print("You open the safe with the keycard and find important" + 
                    " documents.")
                    remove_interactable(main.current_position, "Safe")
                    self.remove_from_inventory("Keycard")
                else:
                    print("You need a keycard to open the safe.")
            elif action2 == "Computer":
                print("You hack the computer and find a photo of Robert Knox."+
                     "You print it out and keep it with you.")
                self.add_to_inventory("Robert Knox's picture")
            elif action2 == "Wrench":
                self.add_to_inventory("Wrench")
                remove_interactable(main.current_position, "Wrench")
            elif action2 == "Hammer":
                self.add_to_inventory("Hammer")
                remove_interactable(main.current_position, "Hammer")
            elif action2 == "Poison Drink" or action2 == "Poison Sierra Knox's Drink":
                print("You see a VIP table with a cup that says"+
                     " 'Congrats Sierra for your win!',"+
                     " knowing she is your target you poison the drink in secret.")
                self.poisoned_drink = True
        
            elif action2 == "Watch Race":
                if not self.racing_car_sabotaged:
                    print("You watch the main spectacle of the venue.")
                    print("When the racers names are called out you see Sierra Knox,"+
                          "one of your targets")
                    print("You realise you could have sabotaged the car and killed her"+ 
                    "and made it look like an accident")
                    print("Anyways there are more ways to kill. ( ͡❛ ͜ʖ ͡❛)✌")
                elif self.racing_car_sabotaged:
                    print("You watch the main spectacle of the venue.") 
                    print("When the racers names are celled out you see Sierra Knox,"+ 
                    " one of your targets")
                    print("You remember you sabotaged the racing car with the name"+ 
                    " Sierra Knox.")
                    print("You smile and wait for the fun to happen")
                    print("As soon as the announcer says GO! nothing happens.")
                    print("A few laps go by and all of a sudden you see Sierra Knox's"+ 
                    " car turning the corner and you see it loses control and crashes"+ 
                    " and explodes immediately. Good kill ( ͡❛ ͜ʖ ͡❛)👌")
                    main.increment_targets()
                else:
                    pass
        
            elif action2 == "Screwdriver":
                self.add_to_inventory("Screwdriver")
                remove_interactable(main.current_position, "Screwdriver")
        
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
                        self.add_to_inventory("Guard Disguise")
                        remove_interactable(main.current_position, "Guard")
                    else:
                        print("You just punch him to death")
                        self.add_to_inventory("Guard Disguise")
                        remove_interactable(main.current_position, "Guard")
                else:
                    print("You bring the guard to a corner and punch him to death.")
                    self.add_to_inventory("Guard Disguise")
                    remove_interactable(main.current_position, "Guard")
        
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
                    self.add_to_inventory("Ted Mendez Disguise")
                    remove_interactable(main.current_position, "Ted Mendez")
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
                    remove_interactable(main.current_position, "Robert Knox")
                elif "Guard Disguise" in inventory:
                    print("You escort Robert Knox to safe room as a safetly protocol.")
                    print("Then you get him to isolate there")
                    print(
                        "You then proceed to assassinate him and dispose of the body.")
                    print("Good work, you killed one of your targets.")
                    increment_targets()
                    check_killed_targets()
                    remove_interactable(main.current_position, "Robert Knox")
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
                    main.increment_targets()
                    main.check_killed_targets()
                    remove_interactable(main.current_position, "Sierra Knox")
        
                elif poisoned_drink:
                    print(
                        "Sierra Knox drinks the poisoned drink that you poisoned earlier")
                    print("Good work, you kill one of your targets")
                    main.increment_targets()
                    main.check_killed_targets()
                    remove_interactable(main.current_position, "Sierra Knox")
        

        
        def interact():
            user_interact = input("Which objects/character would you like to interact?")
            if user_interact in self.actual_interact_list:
                self.task_interact(user_interact)
            elif user_interact in self.character_list:
                self.general_interact_character(user_interact)
            else:
                print("Invalid interactable")
        
        
        def remove_interactable(current_position1, interactable):
            """
            Remove an interactable object/character after interacted with
            """
            if current_position1 in main.map_description:
                room_info = main.map_description[main.current_position]
                if interactable in room_info["interactables"]:
                    room_info["interactables"].remove(interactable)