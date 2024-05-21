class Inventory:
    def __init__(self):
        """
        Start the inventory class with empyt list that will
        have items/interactables added from time to time
        depending on the user.
        """
        self.inventory = []#Inventory List
    
    def add_to_inventory(self, item):
        """
        Add items to the user's inventory
        """
        self.inventory.append(item)
        print(f"{item} has been added to the inventory.")
    
    
    def view_inventory(self):
        """
        Will help the user view inventory.
        """
        if self.inventory:
            print("Inventory: ")
            for item in self.inventory:
                print("-", item)
        else:
            print("Inventory is empty")
    
    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
