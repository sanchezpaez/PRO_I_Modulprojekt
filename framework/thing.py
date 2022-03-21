class Thing:
    def __init__(self, name, description, is_grabbable=False):
        self.name = name
        self.description = description
        self.is_grabbable = is_grabbable


class GrabbableThing(Thing):
    def __init__(self, name, description, use_description, is_infinite, kills):
        super().__init__(name, description, is_grabbable=True)
        self.use_description = use_description
        self.is_infinite = is_infinite
        self.kills = kills


class InfiniteUseThing(GrabbableThing):
    def __init__(self, name, description, use_description, kills=False):
        super().__init__(name, description, use_description, True, kills)

    @staticmethod
    def get_status():
        return "You can use this as many times as you want."


class FiniteUseThing(GrabbableThing):
    def __init__(self, name, description, use_description, status_descriptions, kills=False):
        super().__init__(name, description, use_description, False, kills)
        self.uses = len(status_descriptions)
        self.status_descriptions = status_descriptions

    def get_status(self):
        return f"{self.status_descriptions[self.uses - 1]}\nYou can use this {self.uses} more time(s)."


class SingleUseThing(FiniteUseThing):
    def __init__(self, name, description, use_description, status_description, kills=False):
        super().__init__(name, description, use_description, [status_description], kills)
