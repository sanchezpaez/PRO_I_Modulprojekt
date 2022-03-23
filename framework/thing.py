# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

class Deadliness:
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
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def is_grabbable(self):
        return self.__is_grabbable


class GrabbableThing(Thing):
    """
    A class to represent all Thing instances in the game where is_grabbable = True.
    They can be added to the player's inventory.

    Attributes
    ----------
    is_infinite : bool
        Not specified.
    kills : bool
        Not specified.
    """

    def __init__(self, name, description, use_description, is_infinite, kills):
        super().__init__(name, description, is_grabbable=True)
        self.__use_description = use_description
        self.__is_infinite = is_infinite
        self.__kills = kills

    @property
    def use_description(self):
        return self.__use_description

    @property
    def is_infinite(self):
        return self.__is_infinite

    @property
    def kills(self):
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
    kills : bool
        False is default value.
    """

    def __init__(self, name, description, use_description, status_descriptions, kills=Deadliness.not_deadly):
        super().__init__(name, description, use_description, False, kills)
        self.__uses = len(status_descriptions)
        self.__status_descriptions = status_descriptions

    @property
    def uses(self):
        return self.__uses

    @uses.setter
    def uses(self, new_uses):
        self.__uses = new_uses

    @property
    def status_description(self):
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

    def __init__(self, name, description, use_description, status_description, kills=False, wins=False):
        super().__init__(name, description, use_description, [status_description], kills)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins
