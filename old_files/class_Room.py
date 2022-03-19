# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

from old_files import auxiliary_functions as funct


#

class Room:
    def __init__(self, name, description_file):
        self.name = name
        self.description_file = description_file
        self.connections = {}  # Map of room connections
        self.objects = []  # List of strings
        self.actions = ['get hint', 'leave room']  # Recode as dict, so values can be methods
        self.object_dict = {}

    def print_description(self):
        funct.read_file(self.description_file)
        #print(f"What do you want to do? {player.actions_commands}")

    def get_connections(self):
        return self.connections

    def get_hint(self):
        print("This is a hint.")

    def add_object(self, object):
        self.objects.append(object)

    def remove_object(self, object):
        self.objects.remove(object)
        return object

    def print_objects(self):
        for object in self.objects:
            print(object.get_name())

    def get_actions(self):
        for action in self.actions:
            print(action)

    def get_objects(self):
        return self.objects

    def get_object_name_list(self):
        object_name_list = []
        for object in self.objects:
            name = object.get_name()
            object_name_list.append(name)
        return object_name_list

    def get_object_dict(self):
        return self.object_dict

    def add_dict_object(self, object):
        self.object_dict[object.get_name()] = object.print_description_obj()

    # def get_values_objects_dict(self):
    #     object_list = []
    #     for item in self.object_dict:
    #         object = item.
    #         object_list.append(object)
    #     return object_list




    # def get_actions_dict(self):
    #     print(self.actions_dict.keys())

    def add_actions(self, action_list):
        self.actions.extend(action_list)

    def object_list(self):
        object_list = []
        for object in self.objects:
            object_list.append(object.get_name())
        return object_list

    def return_actions(self):
        return self.actions



