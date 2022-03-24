# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022


from framework.framework_game import Game

from please_the_cat_rooms import kitchen, bathroom, bedroom,\
    living_room, garden, cellar, hall, hof, \
    neighbours

# Game created using the classes of the attached folder 'framework'

if __name__ == '__main__':
    kitchen.east_room = bathroom
    kitchen.south_room = bedroom
    kitchen.north_room = living_room
    kitchen.west_room = garden
    bathroom.west_room = kitchen
    bathroom.north_room = cellar
    bathroom.east_room = neighbours
    bedroom.north_room = kitchen
    living_room.south_room = kitchen
    living_room.east_room = cellar
    living_room.west_room = hof
    garden.east_room = kitchen
    garden.north_room = hof
    cellar.south_room = bathroom
    cellar.west_room = living_room
    hall.south_room = living_room
    hof.south_room = garden
    hof.east_room = living_room
    neighbours.west_room = bathroom
    game = Game(name="Please the Cat",
                description="You love your cat, but she is very annoying "
                            "when she doesn't find her toy. \n"
                            "Find it and she will stop meowing.",
                starting_room=kitchen)
    game.play()
