# -*- coding: utf-8 -*-
# Modulprojekt PRO1
# Authorin: Sandra Sánchez
# Datum: 16.02.2022

import class_Player as P
import class_Room
import main

class Thing:
    def __init__(self, name, description):
        self.name = name  # It's a string
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

class Grabbable(Thing):
    def __init__(self, name, description, use_description):
        super().__init__(name, description)
        self.contents = []
        self.open = False
        self.used = False
        self.edible = False
        self.moved = False
        self.description = description
        self.name = name
        self.use_description = use_description


class Disposable(Grabbable):
    def __init__(self, name, description, use_description):
        super().__init__(name, description, use_description)

    def __del__(self):
        pass

    def use(self):
        P.Player.remove_from_inventory(self)
        self.used = True
        return self.use_description

class MultipleUse(Grabbable):
    def __init__(self, name, description, use_description, number_uses):
        super().__init__(name, description, use_description)
        self.number_uses = number_uses

    def use(self):
        while self.number_uses > 0:
            self.number_uses -= 1
            return self.use_description
        else:
            print("I'm afraid you can't use that anymore.")

    def get_uses(self):
        return self.number_uses
