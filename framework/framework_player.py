# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

from framework.framework_thing import FiniteUseThing, SingleUseThing, Deadliness


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
        """Getter for self.__name, returns a str."""
        return self.__name

    @property
    def description(self):
        """Getter for self.__description, returns a str."""
        return self.__description

    @property
    def lives(self):
        """Getter for self.__lives, returns an int."""
        return self.__lives

    @lives.setter
    def lives(self, new_lives):
        """Setter for self.__lives, returns an int."""
        self.__lives = new_lives

    @property
    def inventory(self):
        """Getter for self.__inventory, returns a list of Grabbable objects."""
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
            return f"Congrats, {self.name} -- you definitely are {self.description}!\nYou win the game :)"
        else:
            if thing.kills == Deadliness.deadly:
                self.subtract_lives()
                if self.lives == 0:
                    return f"You're dead, {self.name}!  Be {self.description}-er next time!  GAME OVER."
                else:
                    print(
                        "That was a near-to-death experience. But what doesn't kill you, makes you stronger (kind of).")
                    print(f"You have {self.lives} lives left.")
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
        """Subtract 1 life from player."""
        self.lives -= 1
