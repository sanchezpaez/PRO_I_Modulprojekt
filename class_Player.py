# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

class Being:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def talk(self, spoken_sounds):
        return spoken_sounds

class Animal(Being):
    def __init__(self, name, description):
        super().__init__(name, description)

class Player(Being):
    def __init__(self, name, description, location):
        super().__init__(name, description)
        self.location = location
        self.inventory = []
        self.lives = 3
        self.actions_commands = [
            'watch', 'go to', 'grab', 'talk to', 'push',
            'pull', 'open']

    def get_inventory(self):
        inventory_list = []
        for object in self.inventory:
            inventory_list.append(object.get_name())
        print(f"You have {inventory_list}")

    def remove_from_inventory(self, Disposable):
        self.inventory.remove(Disposable)