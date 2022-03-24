# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

class Room:
    """
    A class to represent the accessible locations.
    Attributes
    ----------
    name : str
        Name of the room.
    description : str
        Description of the room.
    things : list of Thing instances.
        Inventory of the room.
    self.north_room: None
        Room to be set a posteriori. Location accessible to the north.
    self.south_room: None
        Room to be set a posteriori. Location accessible to the south.
    self.east_room: None
        Room to be set a posteriori. Location accessible to the north.
    self.west_room: None
        Room to be set a posteriori. Location accessible to the north.
    """

    def __init__(self, name, description, things):
        self.__name = name
        self.__things = things
        self._description = description
        self.__north_room = None
        self.__south_room = None
        self.__east_room = None
        self.__west_room = None

    @property
    def name(self):
        """Getter for self.__name, returns a str."""
        return self.__name

    @property
    def things(self):
        """Getter for self.__things, returns a list of Thing objects."""
        return self.__things

    @property
    def description(self):
        """Getter for self.__description, returns a str."""
        return self._description

    @property
    def north_room(self):
        """Getter for self.__north_room, returns a Room object."""
        return self.__north_room

    @north_room.setter
    def north_room(self, new_room):
        """Setter for self.__north_room, replaces current Room for another Room object."""
        self.__north_room = new_room

    @property
    def south_room(self):
        """Getter for self.__south_room, returns a Room object."""
        return self.__south_room

    @south_room.setter
    def south_room(self, new_room):
        """Setter for self.__south_room, replaces current Room for another Room object."""
        self.__south_room = new_room

    @property
    def east_room(self):
        """Getter for self.__east_room, returns a Room object."""
        return self.__east_room

    @east_room.setter
    def east_room(self, new_room):
        """Setter for self.__east_room, replaces current Room for another Room object."""
        self.__east_room = new_room

    @property
    def west_room(self):
        """Getter for self.__west_room, returns a Room object."""
        return self.__west_room

    @west_room.setter
    def west_room(self, new_room):
        """Setter for self.__west_room, replaces current Room for another Room object."""
        self.__west_room = new_room

    def leave_room(self):
        """
        Print possible_rooms_names, as for user's input and check if Room is accessible.
        If Room is accessible:
            self.get_room_from_room_name()
        Else:
            print warning message(str).
        """
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
        """
        Match user's input with Room
        If Room is accessible:
            return Room
        Else:
            print warning message(str)
            return None.
        """
        if room_name in self.possible_rooms_names():
            room = [room for room in self.possible_rooms() if room_name == room.name][0]
            return room
        else:
            print("Is that even a place?")
            return None

    def possible_rooms_names(self):
        """
        Return list of accessible rooms.names
        :rtype: str
        """
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
        """
        Return list of accessible rooms.
        :rtype: Room
        """
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
        """
        Print all things' names in inventory of Room.
        :rtype: str
        """
        for thing in self.get_things_names():
            print(thing)

    def remove(self, thing):
        """Remove an instance of Thing from Room inventory."""
        self.things.remove(thing)

    def get_things_names(self):
        """
        Return all things' names in inventory of Room.
        :rtype: str
        """
        things_names = [thing.name for thing in self.things]
        return things_names


class SpecialRoom(Room):
    """
    A class to represent the Room that contains the winning condition(special_thing).
    Attributes
    ----------
    name : str
        Name of the room.
    description : str
        Description of the room.
    second_description : str
        Description of the room after the room has been left.
    things : list of Thing instances.
        Inventory of the room.
    special_thing: instance of Thing class
    It triggers the winning of the game once it is used.
    """

    def __init__(self, name, description, second_description, things, special_thing):
        super().__init__(name, description, things)
        self._second_description = second_description
        self.__special_thing = special_thing

    def leave_room(self):
        """
        Call super().leave_room().
        Set self.description to second_description
        Add special_thing to room's inventory
        :rtype: Room
        """
        new_room = super().leave_room()
        self._description = self._second_description
        self.things.append(self.__special_thing)
        return new_room
