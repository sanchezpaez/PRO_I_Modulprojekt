# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022


import sys

import time

import auxiliary_functions as funct


class Game:
    def __init__(self, name, description_file):
        self.name = name
        self.description_file = description_file
        self.exit_commands = ['exit', 'quit', 'bye', 'end', 'finish']


    def start_game(self):
        print(f"Welcome to {self.name}!")
        time.sleep(1)
        print("What is your name?")
        answer = input('>')
        print(f"Alright! Then welcome to {self.name}, {answer}!")
        time.sleep(1)
        funct.read_file(self.description_file)
        time.sleep(2)

    @staticmethod
    def exit_game():
        print('BYE! See you next time :)')
        sys.exit()

    def restart_game(self):
        yes = ['y', 'yes', 'yeah', 'yep']
        print("Are you sure you want to exit?")
        answer = input('>')
        if answer.lower() in yes:
            self.exit_game()
        else:
            self.start_game()


class Room:
    def __init__(self, name, description_file):
        self.name = name
        self.description_file = description_file
        self.connections = {}
        self.objects = []  # List of strings
        self.actions = []

    def get_description(self):
        funct.read_file(self.description_file)
        #print(f"What do you want to do? {player.actions_commands}")

    def add_object(self, object):
        self.objects.append(object)

    def remove_object(self, object):
        self.objects.remove(object)
        return object

    def get_object(self, object):
        return self.objects[object]


class Thing:
    def __init__(self, name, description):
        self.name = name  # It's a string
        self.description = description

    def get_description(self):
        return self.description

class Grabbable(Thing):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.contents = []
        self.open = False
        self.used = False


class Disposable(Grabbable):
    pass

class MultipleUse(Grabbable):
    pass


class Being:
    def __init__(self, name):
        self.name = name

    def talk(self, spoken_sounds):
        return spoken_sounds

class Animal(Being):
    def __init__(self, name):
        super().__init__(name)

class Player(Being):
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location
        self.inventory = []
        self.lives = 3
        self.actions_commands = [
            'watch', 'go to', 'grab', 'talk to', 'push',
            'pull', 'open']


if __name__ == '__main__':
    please_cat_game = Game('Please the cat', '../test.txt')
    please_cat_game.start_game()
    player = Player('Sandra', 'kitchen')
    kitchen = Room('kitchen', '../kitchen.txt')
    garden = Room('garden', '../garden.txt')
    bathroom = Room('bathroom', '../bathroom.txt')
    bedroom = Room('bedroom', '../bedroom.txt')
    living_room = Room('living_room', '../living_room.txt')
    kitchen.connections = {'north' : living_room, 'south' : bedroom, 'east' : bathroom, 'west' : garden}
    kitchen.get_description()
    kitchen.add_object('mayonnaise')
    mayonnaise = Grabbable('mayonnaise', "It doesn't look really fresh, but you're starving...")
    kitchen.add_object('knife')
    bathroom.add_object('brush')
    bathroom.add_object('towel')
    bedroom.add_object('bra')
    bedroom.add_object('furball')
    living_room.add_object('book')
    living_room.add_object('balalaika')
    kitchen.actions = ['inspect', 'leave room', 'grab']

    response = ''
    while response not in please_cat_game.exit_commands:
        print('What do you want to do?')
        for action in kitchen.actions:
            print(action)
        response = input('>')



