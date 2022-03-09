# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

import auxiliary_functions as funct

class Room:
    def __init__(self, name, description_file):
        self.name = name
        self.description_file = description_file
        self.connections = {}  # Map of room connections
        self.objects = []  # List of strings
        self.actions = ['exit game', 'get hint', 'leave room', 'get inventory']  # Recode as dict, so values can be methods

    def get_description(self):
        funct.read_file(self.description_file)
        #print(f"What do you want to do? {player.actions_commands}")

    def add_object(self, object):
        self.objects.append(object)

    def remove_object(self, object):
        self.objects.remove(object)
        return object

    def get_objects(self):
        for object in self.objects:
            print(object.get_name())

    def get_actions(self):
        for action in self.actions:
            print(action)

    def add_actions(self, action_list):
        self.actions.extend(action_list)

    def object_list(self):
        object_list = []
        for object in self.objects:
            object_list.append(object.get_name())
        return object_list

