from thing import Thing


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
