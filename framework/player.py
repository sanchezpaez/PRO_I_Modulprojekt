# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

import sys

from framework import game
from framework.thing import FiniteUseThing, SingleUseThing


class Player:
    """
    A class to represent the game's user.
    Attributes
    ----------
    name : str
        Name of the player
    description : str
        Self description of player
    lives : int
        Opportunities to win the game until the game exits
    """
    def __init__(self, name, description, lives):
        self.__name = name
        self.__description = description
        self.__lives = lives
        self.__inventory = []

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, new_lives):
        self.__lives = new_lives

    @property
    def inventory(self):
        return self.__inventory

    def get_inventory_names(self):
        """
        Return names of Thing objects in inventory
        :rtype: str
        """
        return [thing.name for thing in self.inventory]

    def print_inventory(self):
        """
        Print names of Thing objects in the player's inventory
        :rtype: str
        """
        if not self.inventory:
            print("Your pockets are empty.")
        else:
            print("This stuff is in your pockets:")
            for item in self.inventory:
                print(f"{item.name} - {item.get_status()}")

    def grab(self, thing):
        """Print grab message and add Thing to player's inventory."""
        print(f"You grabbed the {thing.name}.")
        self.inventory.append(thing)

    def use(self, thing):
        """
        Print use description of Thing instance.
        If thing.wins:
            print message and exit the program.
        Else:
            if thing.kills: call subtract_lives()
            else: print message.
        """
        print(thing.use_description)
        if isinstance(thing, SingleUseThing) and thing.wins:
            # print(f"Congrats, {self.name} -- you definitely are {self.description}!\nYou win the game :)")
            # sys.exit()
            return f"Congrats, {self.name} -- you definitely are {self.description}!\nYou win the game :)"
        else:
            if thing.kills:
                self.subtract_lives()
            if isinstance(thing, FiniteUseThing):
                thing.uses -= 1
                if thing.uses == 0:
                    print(f"There is no {thing.name} left.")
                    self.inventory.remove(thing)
                else:
                    print(thing.get_status())
            else:
                print("You can use this as many times as you want.")

    def subtract_lives(self):
        """
        Subtract 1 life from player.
        If self.lives == 0:
            self.die()
        else:
            print message with remaining lives.
        """
        self.lives -= 1
        if self.lives == 0:
            self.die()
        else:
            print("That was a near-to-death experience. But what doesn't kill you, makes you stronger (kind of).")
            print(f"You have {self.lives} lives left.")

    def die(self):
        """Print personalised message and exit game."""
        print(f"You're dead, {self.name}!  Be {self.description}-er next time!  GAME OVER.")
        sys.exit()  # We cannot access exit_game from the player  bc it's on the game level
        # implement restart
        #todo: create player?
