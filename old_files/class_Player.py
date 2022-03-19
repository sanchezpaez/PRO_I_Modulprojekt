# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

import main as m
import class_Thing as T

class Being:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def talk(self, spoken_sounds):
        return spoken_sounds

# class Animal(Being):
#     def __init__(self, name, description):
#         super().__init__(name, description)

class Player(Being):
    def __init__(self, name, description, lives, location):
        super().__init__(name, description)
        self.location = location
        self.description = description
        self.inventory = []
        self.lives = lives
        # self.actions_commands = [
        #     'watch', 'go to', 'grab', 'talk to', 'push',
        #     'pull', 'open']

    def get_lives(self):
        return self.lives

    def get_location(self):
        return self.location

    def get_inventory(self):
        return self.inventory

    def print_inventory(self):
        inventory_list = []
        for object in self.inventory:
            inventory_list.append(object.get_name())
        while inventory_list:
            print(f"You have {inventory_list}")
        else:
            print("Your pockets are empty.")

    def leave_room(self, current_location):
        print("In which direction do you want to move?: north, south, east, west")
        answer = input('>')
        if answer not in self.location.get_connections().keys():
            m.Game.tiping_mistake()  # Givers error if I try to call the cat-game instance
        else:
            print(f"You go {answer}")  # Make a function for this so we don't repeat code
            self.location = self.location.connections[answer]
            self.location.print_description()

    def inspect(self): # isinstance object of class Thing
        print("What do you want to inspect?")
        self.location.print_objects()
        response = input('>')
        if response in self.location.get_object_dict().keys():
            print(self.location.get_object_dict().keys())  # dict_keys(['mayonnaise', 'knife'])
            # Call Thing.get_description() by accessing value (object that corresponds to string)
            print(self.location.get_object_dict())  # Prints None?
            T.Thing.get_description(object)
        else:
            m.Game.tiping_mistake()
        # if object_name == self.location.get_objects.__str__():
        #     self.location.get_objects.get_description()
        # else:
        #     m.Game.tiping_mistake()

        #print(self.location.get_object_dict())  #{'mayonnaise': <class_Thing.MultipleUse object at 0x109754520>, 'knife': <class_Thing.Grabbable object at 0x1097575b0>}
        # if response in self.location.get_object_name_list():
        #     print("you can do that")
        #     # return T.Thing.get_description(object)

        # if response in self.location.get_object_dict().keys():
        #     print("you can do that")
        #     #Call Thing.get_description() by accessing value (object that corresponds to string)
        #     print(self.location.get_object_dict()[response])
        # else:
        #     m.Game.tiping_mistake()

    def grab(self, object):
        print('You can grab this')
        P.Player.add_to_inventory(self, object)

    # def remove_from_inventory(self, Disposable):
    #     self.inventory.remove(Disposable)
    #
    # def add_to_inventory(self, object):
    #     self.inventory.append(object)
    #
    # def die(self):
    #     while self.lives > 0:
    #         self.lives -= 1
    #     print("That was a near-to-death experience. But what doesn't kill you, makes you stronger (kind of).")
    #     print(f"You have {Player.get_lives()} lives left.")