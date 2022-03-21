# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

import sys
import time

from player import Player
from room import Room
from thing import GrabbableThing, InfiniteUseThing, FiniteUseThing, Thing


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
    kitchen = Room(
        name='kitchen',
        description="You are in the kitchen. One would think there is something here to please that cat of yours. "
                    "Check every item carefully, things are not what they seem...\n\nThere is some mayonnaise and a knife on the table.",
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
                    "It's probably a good idea to start washing your hands, since you're in the bathroom.",
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
    bedroom = Room(
        name='bedroom',
        description="This is the bedroom. "
                    "There is a pile of clothes on the chair. The wardrobe is slightly open.\n",
        things=[
            InfiniteUseThing(
                name='blanket',
                description="Not very clean, but soft and warm.",
                use_description="Mmm...that feels nice."
            ),
            FiniteUseThing(
                name='bubble-maker',
                description="'Catnip bubbles for stressed cats'...I'm wondering what it does to humans.",
                use_description="BLUB...BLUBB...BLUB...Yay!",
                uses=3,
                kills=True
            ),
            Thing(
                name='cat',
                description="That is a catosaur!",
            ) #todo: create animal class
        ],
    )
    living_room = Room(
        name='living-room',
        description="This is the living-room. "
                    "There are toys everywhere. You can also see some books on the shelf.\n",
        things=[
            InfiniteUseThing(
                name='book',
                description="'Woman Rebel. The Margaret Sanger Story', by Peter Bagge.\nSounds cool, I wish I had the time to read it.",
                use_description="The life of the birth-control activist, educator, nurse, mother and protofeminist from her birth..."
            ),
            FiniteUseThing(
                name='Friskies',
                description="Low-quality cat food. Exactly what your cat and you 2 year-old love to eat.",
                use_description="Crunch, crunch...yummy!",
                uses=3,
                kills=True
            ),
            Thing(
                name='window',
                description="You can see the tress blooming and some birds building a nest. Isn't spring wonderful?",
            )
        ],
    )
    garden = Room(
        name='garden',
        description="This is the garden."
                    "The autumn leaves have been there since October, you should find the time to tidy up a bit this space.\n",
        things=[
            InfiniteUseThing(
                name='shovel',
                description="Kid-size shovel. Perfect to dig in the sandbox.",
                use_description="Dig, dig...and a bit more dig."
            ),
            FiniteUseThing(
                name='flower seeds',
                description="Plant at the end of March, water and wait for the miracle to happen.",
                use_description="You planted the seeds, well done! But wait, are those flowers not poisonous?",
                uses=1,
                kills=True
            ),
            Thing(
                name='swing',
                description="You are too heavy for this, don't even dream about it.",
            )
        ],
    )
    cellar = Room(
        name='cellar',
        description="This is the cellar."
                    "A dark and dusty room full of crap, aka spider paradise. \nYou see some bags readily packed to donate to Ukrainian refugees, a pair of shoes and an iflatable boat.\n",
        things=[
            InfiniteUseThing(
                name='Pair of shoes',
                description="Very fancy shoes. Why was it again that you haven't worn them?",
                use_description="Comfy and stylish, perfect for you."
            ),
            FiniteUseThing(
                name='inflatable boat',
                description="Perfect for really hot days at the lake.",
                use_description="Your are using it...in the cellar, so it breaks.",
                uses=1,
                kills=False
            ),
            Thing(
                name='donation bags',
                description="There are clothes, food and toiletries.",
            )
        ],
    )
    hall = Room(
        name='hall',
        description="This is the hall."
                    "A weird place to look for anything, unless your cat has escaped from the flat.",
        things=[
            InfiniteUseThing(
                name='tacky dishes',
                description="Not beautiful, but in one piece.",
                use_description="You may want to put some food on that first, but whatever. I'm not judging there."
            ),
            FiniteUseThing(
                name='box of chocolates',
                description="Not your thing, but you can use them to get your daughters to do what you want.",
                use_description="Mmm...delicious. Wait, what was the expiry date?",
                uses=1,
                kills=True
            ),
            Thing(
                name='mailbox',
                description="Just some bloody Werbung, not worth checking.",
            )
        ],
    )
    kitchen.east_room = bathroom
    kitchen.south_room = bedroom
    kitchen.north_room = living_room
    kitchen.west_room = garden
    bathroom.west_room = kitchen
    bathroom.north_room = cellar
    bedroom.north_room = kitchen
    living_room.south_room = kitchen
    living_room.east_room = cellar
    garden.east_room = kitchen
    cellar.south_room = bathroom
    cellar.west_room = living_room
    hall.south_room = living_room
    game = Game(starting_room=kitchen)
    features = game.generate_player_features()
    game.player = Player(features[0], features[1], features[2])
    game.play()

# example:
# user needs to know about objects
# rooms have objects (Thing)
# user needs to ask about a Thing via a string
# we need to access the correct Thing
