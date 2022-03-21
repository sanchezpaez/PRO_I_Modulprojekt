from framework.room import Room
from please_the_cat_game.please_the_cat_things import pair_of_shoes, inflatable_boat, donation_bags, tacky_dishes, \
    box_of_chocolates, mailbox, shovel, flower_seeds, swing, book, friskies, window, blanket, cat, \
    bubble_maker, hairbands, phone, litter_box, knife, mayo, table, empty_beer_bottle, bicycle, chestnuts, rug, picture

kitchen = Room(
    name='kitchen',
    description="You are in the kitchen. One would think there is something here to please that cat of yours. "
                "Check every item carefully, things are not what they seem...\n\nThere is some mayonnaise and a knife on the table.",
    things=[
        knife, mayo, table
    ],
)
bathroom = Room(
    name='bathroom',
    description="It smells of kind of nice here... mixed with cat pee. Ok, maybe not so nice. \n"
                "It's probably a good idea to start washing your hands, since you're in the bathroom.",
    things=[
        hairbands, phone, litter_box
    ],
)
bedroom = Room(
    name='bedroom',
    description="This is the bedroom. "
                "There is a pile of clothes on the chair. The wardrobe is slightly open.\n",
    things=[
        blanket, bubble_maker, cat
    ],
)
living_room = Room(
    name='living-room',
    description="This is the living-room. "
                "There are toys everywhere. You can also see some books on the shelf.\n",
    things=[
        book, friskies, window
    ],
)
garden = Room(
    name='garden',
    description="This is the garden."
                "The autumn leaves have been there since October, you should find the time to tidy up a bit this space.\n",
    things=[
        shovel, flower_seeds, swing
    ],
)
cellar = Room(
    name='cellar',
    description="This is the cellar."
                "A dark and dusty room full of crap, aka spider paradise. \nYou see some bags readily packed to donate to Ukrainian refugees, a pair of shoes and an iflatable boat.\n",
    things=[
        pair_of_shoes, inflatable_boat, donation_bags
    ],
)
hall = Room(
    name='hall',
    description="This is the hall."
                "A weird place to look for anything, unless your cat has escaped from the flat.",
    things=[
        tacky_dishes, box_of_chocolates, mailbox
    ],
)
hof = Room(
    name='Hof',
    description="This is the Hot. \n"
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
