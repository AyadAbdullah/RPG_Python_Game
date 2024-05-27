import Inventory
from map import map_description

current_position = (0, 0)


class Interact:
    def __init__(self):
        """
        Intialize the invenotry class
        """
        self.inventory = Inventory.Inventory()
        self.poisoned_drink = False
        self.racing_car_sabotaged = False
        self.targets = 0
        self.actual_interact_list = [
            "Security Camera", "Keycard", "Safe", "Computer", "Wrench",
          "Hammer", "Poison Drink", "Poison Sierra Knox's Drink",
          "Watch Race", "Screwdriver", "Racing Car", "Guard"]
        #The above is for actual interactable actions that will help the 
        #user complete the task.
    
        self.character_list = ["Ted Mendez", "Robert Knox", "Sierra Knox"]
        #For character interact which allow the user to kill.
        
    def increment_targets(self):
      """
      This functions add 1 to the global variable target, to 
      ensure if the mission has been complete or not.
      """
      
      self.targets += 1


    def check_killed_targets(self):
      """
      This function checks if both the targets have been killed or not.
      """

      
      if self.targets == 2:
          print("Mission Accomplished. Good Work.")
          return True
      return False
        
    def task_interact(self, action2, current_position):
        global poisoned_drink, racing_car_sabotaged
    
    
        if action2 == "Security Camera":
            print("You disable the camera")
            
        elif action2 == "Keycard":
            print("You find some idiot guard's lost keycard. You pick it up")
            self.inventory.add_to_inventory("Keycard")
            self.remove_interactable(current_position, "Keycard")
            
        elif action2 == "Safe":
            if "Keycard" in self.inventory.inventory:
                print("You open the safe with the keycard and find important" + 
                " documents.")
                self.remove_interactable(current_position, "Safe")
                self.inventory.remove_from_inventory("Keycard")
            else:
                print("You need a keycard to open the safe.")
                
        elif action2 == "Computer":
            print("You hack the computer and find a photo of Robert Knox."+
                 "You print it out and keep it with you.")
            self.inventory.add_to_inventory("Robert Knox's picture")
            
        elif action2 == "Wrench":
            self.inventory.add_to_inventory("Wrench")
            self.remove_interactable(current_position, "Wrench")
            
        elif action2 == "Hammer":
            self.inventory.add_to_inventory("Hammer")
            self.remove_interactable(current_position, "Hammer")
        
        elif action2 == "Screwdriver":
            self.inventory.add_to_inventory("Screwdriver")
            self.remove_interactable(current_position, "Screwdriver")
    
        elif action2 == "Guard":
            weapons = ["Hammer", "Wrench"] 
            available_weapons = [weapon for weapon in weapons if weapon in 
                                 self.inventory.inventory]
    
            if available_weapons:
                print(f"You have {' , '.join(available_weapons)}")
                kill_action = input("Which one do you want to use to kill the guard?")
    
                if kill_action in available_weapons:
                    print(f"You beat the guard with the {kill_action} and kill him"+ 
                          " and take his disguise.")
                    self.inventory.add_to_inventory("Guard Disguise")
                    self.remove_interactable(current_position, "Guard")
                else:
                    print("You just punch him to death")
                    self.inventory.add_to_inventory("Guard Disguise")
                    self.remove_interactable(current_position, "Guard")
            else:
                print("You bring the guard to a corner and punch him to death.")
                self.inventory.add_to_inventory("Guard Disguise")
                self.remove_interactable(current_position, "Guard")
    
        else:
            print("Not a valid interactable object")
    
    def general_interact_character(self, character, current_position):
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
                    "You distract Ted Mendez to a corner, where there is leaf" 
                    +"shredder."
                )
                print(
                    "You then knock him out, take his disguise and dispose his"+ 
                    " body in the"
                    + " leaf shredder.")
                self.inventory.add_to_inventory("Ted Mendez Disguise")
                self.remove_interactable(current_position, "Ted Mendez")
            elif choice2 == 2:
                print("You leave him alone.")
            else:
                print("Invalid Entry, try again")
        elif character == "Robert Knox":
            if ("Ted Mendez Disguise" and "Robert Knox's picture" in 
                self.inventory.inventory):
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
                self.increment_targets()
                self.check_killed_targets()
                self.remove_interactable(current_position, "Robert Knox")
            elif "Guard Disguise" in self.inventory.inventory:
                print("You escort Robert Knox to safe room as a safetly protocol.")
                print("Then you get him to isolate there")
                print(
                    "You then proceed to assassinate him and dispose of the body.")
                print("Good work, you killed one of your targets.")
                self.increment_targets()
                self.check_killed_targets()
                self.remove_interactable(current_position, "Robert Knox")
            else:
                print("You get caught without having a disguise or the picture.")
                print("Mission Failed.☹️")
                exit()
    
        elif character == "Sierra Knox":
            if "Guard Disguise" in self.inventory.inventory:
                print("You escort Sierra Knox to a safe room as a safely protocol.")
                print("Then you get him to isolate there")
                print(
                    "You then proceed to assassinate her and dispose of the body.")
                print("Good work, you killed one of your targets.")
                self.increment_targets()
                self.check_killed_targets()
                self.remove_interactable(current_position, "Sierra Knox")
    
            else:
                print("Invalid")
    

    
    def interact(self, current_position):
        user_interact = input("Which objects/character would you like to interact?")
        if user_interact in self.actual_interact_list:
            self.task_interact(user_interact, current_position)
        elif user_interact in self.character_list:
            self.general_interact_character(user_interact, current_position)
        else:
            print("Invalid interactable")
    
    
    def remove_interactable(self, current_position, interactable):
        """
        Remove an interactable object/character after interacted with
        """
        room_info = map_description.get(current_position)
        if room_info:    
            interactables = room_info.get("interactables", [])
            if interactable in interactables:
                interactables.remove(interactable)