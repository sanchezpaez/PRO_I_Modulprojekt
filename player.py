import sys

from thing import Thing, FiniteUseThing


class Player:
    def __init__(self, name, description, lives):
        self.name = name
        self.description = description
        self.lives = lives
        self.inventory: list[Thing] = []

    def subtract_lives(self):
        self.lives -= 1
        if self.lives == 0:
            self.die()
        else:
            print("That was a near-to-death experience. But what doesn't kill you, makes you stronger (kind of).")
            print(f"You have {self.lives} lives left.")

    @staticmethod
    def die():
        print("You're dead! GAME OVER.")
        sys.exit()  # We cannot access exit_game from the player  bc it's on the game level
        # implement restart

    def get_inventory_names(self):
        return [thing.name for thing in self.inventory]

    def print_inventory(self):
        if not self.inventory:
            print("Your pockets are empty.")
        else:
            print("This stuff is in your pockets:")
            for item in self.inventory:
                print(f"{item.name} - {item.get_status()}")

    def grab(self, thing):
        print(f"You grabbed the {thing.name}.")
        self.inventory.append(thing)

    def use(self, thing):
        print(thing.use_description)
        if thing.kills:
            self.subtract_lives()
        if isinstance(thing, FiniteUseThing):
            thing.uses -= 1
            if thing.uses == 0:
                print(f"There is no {thing.name} left.")
                self.inventory.remove(thing)
            else:
                print(thing.get_status())
        else:
            print("You can use this as many times as you want.")
