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

class Player:
    def __init__(self, name, description, lives):
        self.name = name
        self.description = description
        self.lives = lives
        self.inventory: list[Thing] = []

    def print_inventory(self):
        if not self.inventory:
            print("Your pockets are empty.")
        else:
            print("This stuff is in your pockets:")
            for item in self.inventory:
                print(item.name)

    def grab(self, thing):
        print(f"You grabbed the {thing.name}.")
        self.inventory.append(thing)

    def use(self, thing):
        print(thing.use_description)
        if thing.name == 'mayo':
            self.lives -= 1


class Room:
    def __init__(self, name, description, things):
        self.name = name
        self.things: list[Thing] = things
        self.things_names = [thing.name for thing in self.things]
        self.description = description

    def print_things(self):
        for thing in self.things_names:
            print(thing)

class Thing:
    def __init__(self, name, description, is_grabbable=False):
        self.name = name
        self.description = description
        self.is_grabbable = is_grabbable

class GrabbableThing(Thing):
    def __init__(self, name, description, use_description, is_infinite=False):
        super().__init__(name, description, is_grabbable=True)
        self.use_description = use_description
        self.is_infinite = is_infinite

class InfiniteUseThing(GrabbableThing):
    def __init__(self, name, description, use_description):
        super().__init__(name, description, use_description, is_infinite=True)


class Game:
    def __init__(self):
        self.description = "Intro how to play the game.\n"
        self.current_room = Room(
            'kitchen',
            "You are in the kitchen. One would think there is something here to please that cat of yours. "
            "Check every item carefully, things are not what they seem...\n\nThere is some mayonnaise and a knife on the table." ,
            [
                InfiniteUseThing('knife', "It doesn't look very sharp, but it works.", "zim zam zum"),
                GrabbableThing('mayo', "It doesn't look really fresh, but you're starving...", "there you go, just a spoon full of...mayonnaise..."),
                Thing('table', "This looks heavy.")
            ]
        )
        self.player: Player = None

    def generate_player_features(self):
        print("What is your name?")
        name = input('>')
        time.sleep(1)
        print(f"Welcome to 'Please the Cat', {name}!")
        time.sleep(1)
        print("How would you describe yourself?")
        description = input('>')
        time.sleep(1)
        print(f"'{description}', I'll remember that.")
        lives = self.choose_number()
        time.sleep(1)
        print(f"Ok. You will start the game with {lives} lives. If you lose you can choose to play again.")
        time.sleep(1)
        return name, description, lives

    def choose_number(self):
        number = 0
        print("Choose a number from 1 to 5?")
        chosen_number = int(input('>'))
        if chosen_number in range(1,6):
            number = chosen_number
        else:
            print("Wrong number")
            self.choose_number()
        return number

    @staticmethod
    def print_warning():
        print("Are you sure that is what you are trying to say?")

    def play(self):
        print(self.description)
        while True:
            print()
            print()
            print(self.current_room.description)
            print("\nWhat do you want to do?")
            print("\nexit game  inspect  grab  check inventory")
            response = input(">")
            if response == "exit game":
                self.exit_game()
            elif response == "inspect":
                self.inspect()
            elif response == "grab":
                thing_to_grab = self.ask_for_thing_to_grab()
                if isinstance(thing_to_grab, GrabbableThing):
                    self.player.grab(thing_to_grab)
            elif response == "check inventory":
                self.player.print_inventory()
            else:
                self.print_warning()

    def ask_for_thing_to_grab(self):
        print("What do you want to grab?")
        self.current_room.print_things()
        user_input = input(">")
        if user_input in self.current_room.things_names:
            thing = [thing for thing in self.current_room.things if user_input == thing.name][0]
            if thing.is_grabbable:
                return thing
            else:
                print("You cannot grab this.")
                return None
        else:
            self.print_warning()
            return None

    def exit_game(self):
        self._exit('BYE! See you next time :)')

    def inspect(self):
        print("What do you want to inspect?")
        self.current_room.print_things()
        user_input = input(">")
        if user_input in self.current_room.things_names:
            thing = [thing for thing in self.current_room.things if user_input == thing.name][0]
            print(thing.description)
            print("\nWhat do you want to do?")
            print("\nuse  grab  cancel")
            response = input(">")
            if response == "use":
                self.player.use(thing)  # gives kitchen description again? Remove that
                if self.player.lives < 1:
                    self.game_over()
                #user dies if mayo's uses == 1
                #Remove mayo, change number of uses
            elif response == "grab":
                self.player.grab(thing)
            elif response == "cancel":
                pass
            else:
                self.print_warning()
        else:
            self.print_warning()


    def _exit(self, message):
        print(message)
        sys.exit()

    def game_over(self):
        self._exit("You're dead. Be smarter next time.")



if __name__ == '__main__':
    game = Game()
    features = game.generate_player_features()
    game.player = Player(features[0], features[1], features[2])
    game.play()

# example:
# user needs to know about objects
# rooms have objects (Thing)
# user needs to ask about a Thing via a string
# we need to access the correct Thing