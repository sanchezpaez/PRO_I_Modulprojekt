# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

from framework.framework_room import Room, SpecialRoom
from please_the_cat_things import pair_of_shoes, inflatable_boat, donation_bags, tacky_dishes, \
    box_of_chocolates, mailbox, shovel, flower_seeds, swing, book, friskies, window, blanket, cat, \
    bubble_maker, hairbands, phone, litter_box, knife, mayo, table, empty_beer_bottle, bicycle, chestnuts, rug, picture, \
    toy

kitchen = SpecialRoom(
    name='kitchen',
    description="You are in the kitchen. One would think there is something here to please that cat of yours. "
                "Check every item carefully, things are not what they seem...\n\nThere is some mayonnaise and a knife on the table.",
    second_description="You are in the kitchen again. Wait a minute...Somebody has been here. There is something white and dirty under the table...",
    things=[
        knife, mayo, table
    ],
    special_thing=toy,
)
bathroom = Room(
    name='bathroom',
    description="It smells kind of nice here... mixed with cat pee. Ok, maybe not so nice. \n"
                "It's probably a good idea to start washing your hands, since you're in the bathroom.",
    things=[
        hairbands, phone, litter_box
    ],
)
bedroom = Room(
    name='bedroom',
    description="You are in the bedroom. "
                "There is a pile of clothes on the chair. The wardrobe is slightly open.\n",
    things=[
        blanket, bubble_maker, cat
    ],
)
living_room = Room(
    name='living-room',
    description="You are in the living-room. "
                "There are toys everywhere. You can also see some books on the shelf.\n",
    things=[
        book, friskies, window
    ],
)
garden = Room(
    name='garden',
    description="You are in the garden."
                "The autumn leaves have been there since October, you should find the time to tidy up a bit this space.\n",
    things=[
        shovel, flower_seeds, swing
    ],
)
cellar = Room(
    name='cellar',
    description="You are in the cellar."
                "A dark and dusty room full of crap, aka spider paradise. \nYou see some bags readily packed to donate to Ukrainian refugees, a pair of shoes and an inflatable boat.\n",
    things=[
        pair_of_shoes, inflatable_boat, donation_bags
    ],
)
hall = Room(
    name='hall',
    description="You are in the hall."
                "A weird place to look for anything, unless your cat has escaped from the flat.",
    things=[
        tacky_dishes, box_of_chocolates, mailbox
    ],
)
hof = Room(
    name='Hof',
    description="You are at the Hof. \n"
                "You can see the paper, glass and general rubbish containers. The plastic one is missing (again).",
    things=[
        empty_beer_bottle, bicycle, chestnuts
    ],
)

neighbours = Room(
    name="neighbours'",
    description="This is your neighbours' place.\n"
                "They are used to your cat visiting, so the door is unlocked.",
    things=[
        rug, picture
    ],
)
