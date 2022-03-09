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


class Game:
    def __init__(self, name, description_file):
        self.name = name
        self.description_file = description_file
        self.exit_commands = ['exit', 'quit', 'q', 'e', 'bye', 'end', 'finish']


    def start_game(self):
        print(f"Welcome to {self.name}!")
        time.sleep(1)
        print("What is your name?")
        answer = input('>')
        print(f"Alright! Then welcome to {self.name}, {answer}!")
        time.sleep(1)
        funct.read_file(self.description_file)
        time.sleep(2)

    @staticmethod
    def exit_game():
        print('BYE! See you next time :)')
        sys.exit()

    # class method?
    def restart_game(self):
        yes = ['y', 'yes', 'yeah', 'yep']
        print("Are you sure you want to exit?")
        answer = input('>')
        if answer.lower() in yes:
            self.exit_game()
        else:
            self.start_game()










if __name__ == '__main__':
    please_cat_game = Game('Please the cat', 'test.txt')
    please_cat_game.start_game()
    kitchen = R.Room('kitchen', 'kitchen.txt')
    player = P.Player('Sandra', 'Loving cats since 1982', kitchen)
    garden = R.Room('garden', 'garden.txt')
    bathroom = R.Room('bathroom', 'bathroom.txt')
    bedroom = R.Room('bedroom', 'bedroom.txt')
    living_room = R.Room('living_room', 'living_room.txt')
    hall = R.Room('hall', 'hall.txt')
    Hof = R.Room('Hof', 'hof.txt')
    cellar = R.Room('cellar', 'cellar.txt')
    neighbours = R.Room('neighbours', 'neighbours.txt')
    kitchen.connections = {'north' : living_room, 'south' : bedroom, 'east' : bathroom, 'west' : garden}
    living_room.connections = {'north' : hall, 'south' : kitchen, 'east' : cellar, 'west' : Hof}
    bathroom.connections = {'north' : cellar, 'south' : 'nothing', 'east' : neighbours, 'west' : kitchen}
    bedroom.connections = {'north': kitchen, 'south': 'nothing', 'east': 'nothing', 'west': 'nothing'}
    garden.connections = {'north': Hof, 'south': 'nothing', 'east': kitchen, 'west': 'nothing'}
    Hof.connections = {'north': 'nothing', 'south': garden, 'east': living_room, 'west': 'nothing'}
    hall.connections = {'north': 'nothing', 'south': living_room, 'east': 'nothing', 'west': 'nothing'}
    cellar.connections = {'north': 'nothing', 'south': bathroom, 'east': 'nothing', 'west': living_room}
    neighbours.connections = {'north': 'nothing', 'south': 'nothing', 'east': 'nothing', 'west': bathroom}
    kitchen.get_description()
    mayonnaise = T.MultipleUse('mayonnaise', "It doesn't look really fresh, but you're starving...",
                             "there you go, just a spoon full of...mayonnaise...", 3)
    kitchen.add_object(mayonnaise)
    knife = T.Grabbable('knife', "It doesn't look very sharp, but it works.", "zim zam zum")
    kitchen.add_object(knife)
    bathroom.add_object('brush')
    bathroom.add_object('towel')
    bedroom.add_object('bra')
    bedroom.add_object('furball')
    living_room.add_object('book')
    living_room.add_object('balalaika')
    kitchen.add_actions(['inspect', 'grab'])

    response = ''
    while response.lower() not in please_cat_game.exit_commands:
        print('What do you want to do?')
        time.sleep(2)
        R.Room.get_actions(player.location)
        time.sleep(1)
        response = input('>')
        print(f"{response} what?")
        R.Room.get_objects(player.location)
        response = input('>')

        if response not  in R.Room.object_list(player.location):
            print('Command not valid')
        else:
            # MultipleUse.use(response)
            print("What doesn't kill you makes you stronger.")
            kitchen.remove_object(mayonnaise)
            player.inventory += response
