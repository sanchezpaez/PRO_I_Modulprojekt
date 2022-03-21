from thing import Thing, pair_of_shoes, inflatable_boat, donation_bags, tacky_dishes, \
    box_of_chocolates, mailbox, shovel, flower_seeds, swing, book, friskies, window, blanket, cat, \
    bubble_maker, hairbands, phone, litter_box, knife, mayo, table, empty_beer_bottle, bicycle, chestnuts, rug, picture


class Room:
    def __init__(self, name, description, things):
        self.name = name
        self.things: list[Thing] = things
        self.description = description
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None

    def leave_room(self):
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
        if room_name in self.possible_rooms_names():
            room = [room for room in self.possible_rooms() if room_name == room.name][0]
            return room
        else:
            print("Is that even a place?")
            return None

    def possible_rooms_names(self):
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
        for thing in self.get_things_names():
            print(thing)

    def remove(self, thing):
        self.things.remove(thing)

    def get_things_names(self):
        things_names = [thing.name for thing in self.things]
        return things_names


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
