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

    def subtract_lives(self):
        self.lives -= 1
        if self.lives == 0:
            self.die()
        else:
            print("That was a near-to-death experience. But what doesn't kill you, makes you stronger (kind of).")
            print(f"You have {self.lives} lives left.")


    @staticmethod
    def die():
        print("You're dead! GAME OVER.")
        sys.exit()  # We cannot access exit_game from the player  bc it's on the game level
        #implement restart

    def get_inventory_names(self):
        return [thing.name for thing in self.inventory]

    def print_inventory(self):
        if not self.inventory:
            print("Your pockets are empty.")
        else:
            print("This stuff is in your pockets:")
            for item in self.inventory:
                print(f"{item.name} - {item.get_status()}")

    def grab(self, thing):
        print(f"You grabbed the {thing.name}.")
        self.inventory.append(thing)


    def use(self, thing):
        print(thing.use_description)
        if thing.kills:
            self.subtract_lives()
        if isinstance(thing, FiniteUseThing):
            thing.uses -= 1
            if thing.uses == 0:
                print(f"There is no {thing.name} left.")
                self.inventory.remove(thing)
            else:
                print(f"You have {thing.uses} left.")
        else:
            print("You can use this as many times as you want.")


class Room:
    def __init__(self, name, description, things):
        self.name = name
        self.things: list[Thing] = things
        self.description = description
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None

    def leave_room(self):
        print("Where do you want to go?")
        if self.possible_rooms_names():
            for room in self.possible_rooms_names():
                print(room)
            user_input = input(">")
            if user_input in self.possible_rooms_names():
                print(f"You move to the {user_input}.")
                return self.get_room_from_room_name(user_input)
            else:
                print("Is that even a place?")
        else:
            print("You cannot go anywhere.")

    def get_room_from_room_name(self, room_name):
        if room_name in self.possible_rooms_names():
            room = [room for room in self.possible_rooms() if room_name == room.name][0]
            return room
        else:
            print("Is that even a place?")
            return None


    def possible_rooms_names(self):
        rooms = []
        if self.north_room:
            rooms.append(self.north_room.name)
        if self.south_room:
            rooms.append(self.south_room.name)
        if self.east_room:
            rooms.append(self.east_room.name)
        if self.west_room:
            rooms.append(self.west_room.name)
        return rooms

    def possible_rooms(self):
        rooms = []
        if self.north_room:
            rooms.append(self.north_room)
        if self.south_room:
            rooms.append(self.south_room)
        if self.east_room:
            rooms.append(self.east_room)
        if self.west_room:
            rooms.append(self.west_room)
        return rooms


    def print_things(self):
        for thing in self.get_things_names():
            print(thing)

    def remove(self, thing):
        self.things.remove(thing)

    def get_things_names(self):
        things_names = [thing.name for thing in self.things]
        return things_names



class Thing:
    def __init__(self, name, description, is_grabbable=False):
        self.name = name
        self.description = description
        self.is_grabbable = is_grabbable

class GrabbableThing(Thing):
    def __init__(self, name, description, use_description, is_infinite, kills):
        super().__init__(name, description, is_grabbable=True)
        self.use_description = use_description
        self.is_infinite = is_infinite
        self.kills = kills

class InfiniteUseThing(GrabbableThing):
    def __init__(self, name, description, use_description, kills=False):
        super().__init__(name, description, use_description, True, kills)

    @staticmethod
    def get_status():
        return "You can use this as many times as you want."

class FiniteUseThing(GrabbableThing):
    def __init__(self, name, description, use_description, uses, kills=False):
        super().__init__(name, description, use_description, False, kills)
        self.uses = uses

    def get_status(self):
        if self.uses >= 3:
            return "This is in ok condition."
        elif self.uses == 2:
            return "This is not looking great."
        else:
            return "Almost broken."



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
                self.current_room = new_room
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
    kitchen = Room(
            name='kitchen',
            description="You are in the kitchen. One would think there is something here to please that cat of yours. "
                        "Check every item carefully, things are not what they seem...\n\nThere is some mayonnaise and a knife on the table." ,
            things=[
                InfiniteUseThing(
                    name='knife',
                    description="It doesn't look very sharp, but it works.",
                    use_description="zim zam zum"
                ),
                FiniteUseThing(
                    name='mayo',
                    description="It doesn't look really fresh, but you're starving...",
                    use_description="there you go, just a spoon full of...mayonnaise...",
                    uses=3,
                    kills=True
                ),
                Thing(
                    name='table',
                    description="This looks heavy.",
                )
            ],
        )
    bathroom = Room(
            name='bathroom',
            description="It smells of kind of nice here... mixed with cat pee. Ok, maybe not so nice. \n"
                        "It's probably a good idea to start washing your hands, since you're in the bathroom." ,
            things=[
                # InfiniteUseThing(
                #     name='knife',
                #     description="It doesn't look very sharp, but it works.",
                #     use_description="zim zam zum"
                # ),
                # FiniteUseThing(
                #     name='mayo',
                #     description="It doesn't look really fresh, but you're starving...",
                #     use_description="there you go, just a spoon full of...mayonnaise...",
                #     uses=3,
                #     kills=True
                # ),
                # Thing(
                #     name='table',
                #     description="This looks heavy.",
                # )
            ],
        )
    kitchen.east_room = bathroom
    bathroom.west_room = kitchen
    game = Game(starting_room=kitchen)
    features = game.generate_player_features()
    game.player = Player(features[0], features[1], features[2])
    game.play()

# example:
# user needs to know about objects
# rooms have objects (Thing)
# user needs to ask about a Thing via a string
# we need to access the correct Thing