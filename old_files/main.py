# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

import sys

import time

from old_files import auxiliary_functions as funct, class_Player as P, class_Room as R, class_Thing as T


class Game:
    def __init__(self, name, description_file):
        self.name = name
        self.description_file = description_file
        self.exit_commands = ['exit', 'quit', 'q', 'e', 'bye', 'end', 'finish', 'exit game']
        # implement other commands and add functions with if statements and remove from room class




    def start_game(self):
        print(f"Welcome to {self.name}!")
        time.sleep(2)
        # print("What is your name?")
        # answer = input('>')
        # print(f"Alright! Then welcome to {self.name}, {answer}!")
        time.sleep(1)
        funct.read_file(self.description_file)
        time.sleep(2)
          #NameError: name 'player' is not defined

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

    @staticmethod
    def wrong_command():
        if response not in player.location.return_actions():
            print('Wrong command')

    @staticmethod
    def tiping_mistake():
        print("Are you sure that is what you are trying to say?")

    @staticmethod
    def choose_number():
        global lives
        print("Choose a number from 1 to 5?")
        chosen_number = int(input('>'))
        if chosen_number in range(1,6):
            lives = chosen_number
        else:
            print("Wrong number")
            Game.choose_number()
        return lives

    def generate_player(self):
        print("What is your name?")
        name = input('>')
        time.sleep(1)
        print(f"Welcome to {self.name}, {name}!")
        time.sleep(1)
        print("How would you describe yourself?")
        description = input('>')
        time.sleep(1)
        print(f"'{description}', I'll remember that.")
        lives = Game.choose_number()
        time.sleep(1)
        print(f"Ok. You will start the game with {lives} lives. If you lose you can choose to play again.")
        time.sleep(1)
        return name, description, lives




# def main():
#     player_attributes = Game.generate_player()
#     player = Player(player_attributes[0], player_attributes[1], player_attributes[2], kitchen)

if __name__ == '__main__':
    please_cat_game = Game('Please the cat', 'test.txt')
    please_cat_game.start_game()
    kitchen = R.Room('kitchen', 'kitchen.txt')
    player_attributes = Game.generate_player(please_cat_game)
    player = P.Player(player_attributes[0], player_attributes[1], player_attributes[2], kitchen)
    player.location.print_description()
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
    kitchen.print_description()
    mayonnaise = T.MultipleUse('mayonnaise', "It doesn't look really fresh, but you're starving...",
                             "there you go, just a spoon full of...mayonnaise...", 3)
    kitchen.add_dict_object(mayonnaise)
    kitchen.add_object(mayonnaise)
    knife = T.Grabbable('knife', "It doesn't look very sharp, but it works.", "zim zam zum")
    kitchen.add_object(knife)
    kitchen.add_dict_object(knife)
    bathroom.add_object('brush')
    bathroom.add_object('towel')
    bedroom.add_object('bra')
    bedroom.add_object('furball')
    living_room.add_object('book')
    living_room.add_object('balalaika')
    kitchen.add_actions(['inspect', 'grab'])

    while True:
        response = input('exit game  get inventory  inspect  get hint  leave room\n >')
        response = response.lower().strip()
        if response in please_cat_game.exit_commands:
            please_cat_game.exit_game()
        elif response == 'get inventory':
            player.print_inventory()
        elif response == 'get hint':
            player.location.get_hint()
        elif response == 'leave room':
            player.leave_room(player.location)
        elif response == 'inspect':
            player.inspect()
        else:
            please_cat_game.wrong_command()
        #offer options and ask for input
        #Player gives input and we call function

        # print('What do you want to do?')  # Doesn't suggest exit game (bc we moved it from room.actions)
        # time.sleep(2)
        # R.Room.get_actions(player.location)
        # time.sleep(1)
        # response = input('>')
        # if response in R.Room.return_actions(player.location):
        #     print('Good choice')
        #     if response == 'inspect':
        #         print(f"{response} what?")
        #         R.Room.get_objects(player.location)
        #         response = input('>')
        #         if response not in R.Room.object_list(player.location):
        #             Game.wrong_command()
        #         else:
        #             print('you can do that')
        #             #player.location.inspect(response)
        #             # MultipleUse.use(response)
        #             print("What doesn't kill you makes you stronger.")
        #             kitchen.remove_object(mayonnaise)
        #             player.inventory += response
        # else:
        #     Game.wrong_command()
        #
        #
        #