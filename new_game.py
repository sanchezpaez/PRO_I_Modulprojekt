# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

import sys
import time

from player import Player
from room import kitchen, bathroom, bedroom, living_room, garden, cellar, hall, hof, neighbours
from thing import GrabbableThing


class Game:
    def __init__(self, starting_room):
        self.description = "Intro how to play the game.\n"
        self.current_room = starting_room
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
        if chosen_number in range(1, 6):
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
        self._exit('BYE! See you next time :)')


    def inspect(self):
        print("What do you want to inspect?")
        self.current_room.print_things()
        user_input = input(">")
        if user_input in self.current_room.get_things_names():
            thing = [thing for thing in self.current_room.things if user_input == thing.name][0]
            print(thing.description)
        else:
            self.print_warning()

    def _exit(self, message):
        print(message)
        sys.exit()

    # def game_over(self):
    #     self._exit("You're dead. Be smarter next time.")


if __name__ == '__main__':
    kitchen.east_room = bathroom
    kitchen.south_room = bedroom
    kitchen.north_room = living_room
    kitchen.west_room = garden
    bathroom.west_room = kitchen
    bathroom.north_room = cellar
    bathroom.east_room = neighbours
    bedroom.north_room = kitchen
    living_room.south_room = kitchen
    living_room.east_room = cellar
    living_room.west_room = hof
    garden.east_room = kitchen
    garden.north_room = hof
    cellar.south_room = bathroom
    cellar.west_room = living_room
    hall.south_room = living_room
    hof.south_room = garden
    hof.east_room = living_room
    neighbours.west_room = bathroom
    game = Game(starting_room=kitchen)
    features = game.generate_player_features()
    game.player = Player(features[0], features[1], features[2])
    game.play()

# example:
# user needs to know about objects
# rooms have objects (Thing)
# user needs to ask about a Thing via a string
# we need to access the correct Thing
