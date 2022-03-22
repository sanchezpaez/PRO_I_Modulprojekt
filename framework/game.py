# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

import sys
import time

from framework.thing import GrabbableThing


class Game:
    """
    A class to represent the game.
    Attributes
    ----------
    name : str
        Name of the game
    description : str
        Explains aim of the game
    starting_room : Room
        starting location to __init__ game
    """

    def __init__(self, name, description, starting_room):
        self.name = name
        self.description = description
        self.current_room = starting_room
        self.player = None

    def generate_player_features(self):
        """
        Ask from user's input(str) to generate player's attributes.
        :return:
            attributes name, description, lives(list).
        """
        print("What is your name?")
        name = input('>')
        time.sleep(1)
        print(f"Welcome to '{self.name}', {name}!")
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
        """
        Take user's input (number in specified range) and return integer, that will become the player's lives.
        :return:
            number(int).
        """
        number = 0
        print("Choose a number from 1 to 5?")
        chosen_number = int(input('>'))
        if chosen_number in range(1, 6):
            number = chosen_number
        else:
            print("Wrong number")
            self.choose_number()
        return number

    @staticmethod
    def print_warning():
        """
        Print message(str) when input is unexpected.
        """
        print("Are you sure that is what you are trying to say?")

    def play(self):
        """
        Start game engine and call other methods depending on input, until condition is met (either player's lives == 0
                 or player uses special object).
        """
        print(self.description)
        while True:
            print()
            print()
            print(self.current_room.description)
            print("\nWhat do you want to do?")
            print("\nexit game  inspect  grab  use  leave room  check inventory")
            response = input(">")
            if response == "exit game":
                self.exit_game()
            elif response == "inspect":
                self.inspect()
            elif response == "grab":
                thing_to_grab = self.ask_for_thing_to_grab()
                if isinstance(thing_to_grab, GrabbableThing):
                    self.player.grab(thing_to_grab)
                    self.current_room.remove(thing_to_grab)
            elif response == "use":
                if self.player.inventory:
                    thing_to_use = self.ask_for_thing_to_use()
                    if isinstance(thing_to_use, GrabbableThing):
                        self.player.use(thing_to_use)
                else:
                    print("You have nothing to use in your inventory.")
                    print("Try grabbing something first.")
            elif response == "leave room":
                new_room = self.current_room.leave_room()
                if new_room:
                    self.current_room = new_room
                # todo: if no real room given as input, handle exception (e.g. typing mistake)
            elif response == "check inventory":
                self.player.print_inventory()
            else:
                self.print_warning()

    def ask_for_thing_to_grab(self):
        """
        Offer available options and  take input.
        :return:
             Either Thing or None.
        """
        print("What do you want to grab?")
        self.current_room.print_things()
        user_input = input(">")
        if user_input in self.current_room.get_things_names():
            thing = [thing for thing in self.current_room.things if user_input == thing.name][0]
            if thing.is_grabbable:
                return thing
            else:
                print("You cannot grab this.")
                return None
        else:
            self.print_warning()
            return None

    def ask_for_thing_to_use(self):
        """
        Offer available options and  take input.
        :return:
             Either Thing or None.
        """
        print("What do you want to use?")
        self.player.print_inventory()
        user_input = input(">")
        if user_input in self.player.get_inventory_names():
            thing = [thing for thing in self.player.inventory if user_input == thing.name][0]
            return thing
        else:
            self.print_warning()
            return None

    def exit_game(self):
        """Call self._exit with goodbye message(str)"""
        self._exit('BYE! See you next time :)')

    def inspect(self):
        """
        Offer available options, take input.
        :return:
            print thing description (str).
        """
        print("What do you want to inspect?")
        self.current_room.print_things()
        user_input = input(">")
        if user_input in self.current_room.get_things_names():
            thing = [thing for thing in self.current_room.things if user_input == thing.name][0]
            print(thing.description)
        else:
            self.print_warning()

    def _exit(self, message):
        """Call sys.exit(), offer a message parameter."""
        print(message)
        sys.exit()

