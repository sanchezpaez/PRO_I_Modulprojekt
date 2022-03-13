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
    def __init__(self, name, description, lives, location):
        super().__init__(name, description)
        self.location = location
        self.description = description
        self.inventory = []
        self.lives = lives
        self.actions_commands = [
            'watch', 'go to', 'grab', 'talk to', 'push',
            'pull', 'open']

    def get_lives(self):
        return self.lives

    def print_inventory(self):
        inventory_list = []
        for object in self.inventory:
            inventory_list.append(object.get_name())
        print(f"You have {inventory_list}")

    def remove_from_inventory(self, Disposable):
        self.inventory.remove(Disposable)

    def add_to_inventory(self, object):
        self.inventory.append(object)

    def die(self):
        while self.lives > 0:
            self.lives -= 1
        print("That was a near-to-death experience. But what doesn't kill you, makes you stronger (kind of).")
        print(f"You have {Player.get_lives()} lives left.")