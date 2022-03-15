# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

import class_Room as R
import class_Player as P
import class_Thing as T

import sys

import time

import auxiliary_functions as funct

import sys
from time import sleep


class Room:
    def __init__(self, name, description, things):
        self.name = name
        self.things: list[Thing] = things
        self.things_names = [thing.name for thing in self.things]
        self.description = description

class Thing:
    def __init__(self, name, description, use_description):
        self.name = name
        self.description = description
        self.use_description = use_description

class Game:
    def __init__(self):
        self.description = "Intro how to play the game.\n"
        self.current_room = Room(
            'kitchen',
            "Ok, you are in the kitchen. One would think there is something here to please that cat of yours. Check every item carefully, things are not what they seem...\n\nThere is some mayonnaise and a knife." ,
            [
                Thing('knife', "It doesn't look very sharp, but it works.", "zim zam zum"),
                Thing('mayo', "It doesn't look really fresh, but you're starving...", "there you go, just a spoon full of...mayonnaise...")
            ]
        )

    @staticmethod
    def print_warning():
        print("Are you sure that is what you are trying to say?")

    def play(self):
        print(self.description)
        while True:
            print(self.current_room.description)
            print("\nWhat do you want to do?")
            print("\nexit game  win  inspect")
            response = input(">")
            if response == "win":
                self.win()
            elif response == "exit game":
                self.exit_game()
            elif response == "inspect":
                self.inspect()
            else:
                self.print_warning()

    def exit_game(self):
        self._exit('BYE! See you next time :)')

    def win(self):
        self._exit("You win the game!!!")

    def inspect(self):
        print("What do you want to inspect?")
        for thing in self.current_room.things_names:
            print(thing)
        user_input = input(">")
        if user_input in self.current_room.things_names:
            thing = [thing for thing in self.current_room.things if user_input == thing.name][0]
            print(thing.description)
            print("\nWhat do you want to do?")
            print("\nuse  grab  cancel")
            response = input(">")
            if response == "use":
                print(thing.use_description)
                #Depending on subclass of thing:
                #Remove mayo, change number of uses
            elif response == "grab":
                pass
            elif response == "cancel":
                pass
            else:
                self.print_warning()
        else:
            self.print_warning()


    def _exit(self, message):
        print(message)
        sys.exit()



if __name__ == '__main__':
    game = Game()
    game.play()

# example:
# user needs to know about objects
# rooms have objects (Thing)
# user needs to ask about a Thing via a string
# we need to access the correct Thing