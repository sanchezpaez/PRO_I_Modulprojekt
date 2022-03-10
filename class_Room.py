# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

import auxiliary_functions as funct
#
import main as m

import class_Player as P

class Room:
    def __init__(self, name, description_file):
        self.name = name
        self.description_file = description_file
        self.connections = {}  # Map of room connections
        self.objects = []  # List of strings
        self.actions = ['exit game', 'get hint', 'leave room', 'get inventory']  # Recode as dict, so values can be methods
        # self.actions_dict = {'exit game': Game.exit_game(), 'get hint': self.get_hint(),
        #                  'leave room': Room.leave_room(P.player.location), 'get inventory': P.Player.get_inventory()}

    def get_description(self):
        funct.read_file(self.description_file)
        #print(f"What do you want to do? {player.actions_commands}")

    def get_connections(self):
        return self.connections

    def leave_room(self):
        print("In which direction do you want to move?: north, south, east, west")
        answer = input('>')
        if answer not in Room.get_connections(m.player.location).keys():
            m.Game.tiping_mistake()
        else:
            if answer == 'north':
                pass
            elif answer == 'south':
                pass
            elif answer == 'east':
                pass
            elif answer == 'west':
                pass

    def get_hint(self):
        print("This is a hint.")

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

    def get_actions_dict(self):
        for action in self.actions_dict:
            print(action)

    def add_actions(self, action_list):
        self.actions.extend(action_list)

    def object_list(self):
        object_list = []
        for object in self.objects:
            object_list.append(object.get_name())
        return object_list

    def return_actions(self):
        return self.actions


