# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

class Deadliness:
    """
    Enum class to represent the killing status of FiniteUseThing instances.

    Attributes
    ----------
    not_deadly : bool
        Thing does not subtract player.__lives after use.
    deadly : bool
        Thing does subtract player.__lives after use.
    """
    not_deadly = False
    deadly = True


class Thing:
    """
    A class to represent all objects in the game that can belong to an inventory.

    Attributes
    ----------
    name : str
        Name of the Thing.
    description : str
        Description of the Thing.
    is_grabbable : Boolean
        False by default, if True the Thing is of Grabbable class.
    """

    def __init__(self, name, description, is_grabbable=False):
        self.__name = name
        self.__description = description
        self.__is_grabbable = is_grabbable

    @property
    def name(self):
        """Getter for self.__name, returns a str."""
        return self.__name

    @property
    def description(self):
        """Getter for self.__description, returns a str."""
        return self.__description

    @property
    def is_grabbable(self):
        """Getter for self.__is_grabbable, returns a boolean."""
        return self.__is_grabbable


class GrabbableThing(Thing):
    """
    A class to represent all Thing instances in the game where is_grabbable = True.
    They can be added to the player's inventory.

    Attributes
    ----------
    is_infinite : bool
        Not specified.
    kills : Deadliness
        deadly or not_deadly.
    """

    def __init__(self, name, description, use_description, is_infinite, kills):
        super().__init__(name, description, is_grabbable=True)
        self.__use_description = use_description
        self.__is_infinite = is_infinite
        self.__kills = kills

    @property
    def use_description(self):
        """Getter for self.__use_description, returns a str."""
        return self.__use_description

    @property
    def is_infinite(self):
        """Getter for self.__is_infinite, returns a bool."""
        return self.__is_infinite

    @property
    def kills(self):
        """Getter for self.__kills, returns a Deadliness object."""
        return self.__kills


class InfiniteUseThing(GrabbableThing):
    """
    A class to represent all GrabbableThing instances in the game.
    They can be added to the player's inventory and used for an unlimited number of times.

    Attributes
    ----------
    kills : bool
        Not specified.
    """

    def __init__(self, name, description, use_description, kills=False):
        super().__init__(name, description, use_description, True, kills)

    @staticmethod
    def get_status():
        """Returns infinite status of thing."""
        return "You can use this as many times as you want."


class FiniteUseThing(GrabbableThing):
    """
    A class to represent all FiniteUseThing instances in the game.
    Their status changes after every use.

    Attributes
    ----------
    status_descriptions : str
        Degrading status depending on use.
    status_descriptions : int
        Number of uses left.
    kills : Deadliness
        not_deadly is default value.
    """

    def __init__(self, name, description, use_description, status_descriptions, kills=Deadliness.not_deadly):
        super().__init__(name, description, use_description, False, kills)
        self.__uses = len(status_descriptions)
        self.__status_descriptions = status_descriptions

    @property
    def uses(self):
        """Getter for self.__uses, returns an int."""
        return self.__uses

    @uses.setter
    def uses(self, new_uses):
        """Setter for self.__uses, replaces original value with an int."""
        self.__uses = new_uses

    @property
    def status_description(self):
        """Getter for self.__status_description, returns a str."""
        return self.__status_descriptions

    def get_status(self):
        """Return current status(str) and uses(int) left."""
        return f"{self.__status_descriptions[self.__uses - 1]}\nYou can use this {self.__uses} more time(s)."


class SingleUseThing(FiniteUseThing):
    """
    A class to represent all SingleUseThing instances in the game.
    After they have been used, they are removed from inventory.

    Attributes
    ----------
    wins : bool
        False is default value. The only special_thing will have it set to True.
    """

    def __init__(self, name, description, use_description, status_description, kills=Deadliness.not_deadly, wins=False):
        super().__init__(name, description, use_description, [status_description], kills)
        self.__wins = wins

    @property
    def wins(self):
        """Getter for self.__wins, returns a bool."""
        return self.__wins
