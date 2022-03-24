# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022


from framework.framework_game import Game
from framework.framework_room import Room, SpecialRoom
from framework.framework_thing import InfiniteUseThing, SingleUseThing

wallet = InfiniteUseThing(
    name="wallet",
    description="Just enough money in here.",
    use_description="Infinite money remains.",
)
keys = SingleUseThing(
    name="keys",
    description="Useful to open your front door.",
    use_description="Jingle jangle",
    status_description="Ready to unlock stuff.",
    wins=True,
)

hallway = SpecialRoom(
    name="hallway",
    description="Entrance to your flat.  You're locked-in!",
    second_description="Entrance to your flat.  Looks like you can unlock the door...",
    things=[
        wallet,
    ],
    special_thing=keys,
)
balcony = Room(
    name="balcony",
    description="It's cold out here!",
    things=[],
)

hallway.east_room = balcony
balcony.west_room = hallway

leave_the_flat = Game(
    name="Leave the flat",
    description="You gotta get outta here - cabin fever is setting in.  Leave your flat asap.",
    starting_room=hallway,
)


def test_game(monkeypatch, capsys):
    """
    Test to make sure the program does what it is supposed to do.
    We create new variables to test.
    """

    def simulate_input(text: str):
        """Simulate the user entering a word as input."""
        monkeypatch.setattr('builtins.input', lambda _: text)

    def get_printed_output() -> str:
        """Capture printed output in the terminal."""
        return capsys.readouterr().out

    assert wallet.get_status() == "You can use this as many times as you want."
    assert keys.get_status() == "Ready to unlock stuff.\nYou can use this 1 more time(s)."

    simulate_input("foo")
    assert hallway.leave_room() is None
    assert get_printed_output() == "Where do you want to go?\nbalcony\nIs that even a place?\n"

    simulate_input("balcony")
    assert hallway.leave_room() == balcony
    assert get_printed_output() == "Where do you want to go?\nbalcony\nYou move to the balcony.\n"
