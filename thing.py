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


pair_of_shoes = InfiniteUseThing(
    name='Pair of shoes',
    description="Very fancy shoes. Why was it again that you haven't worn them?",
    use_description="Comfy and stylish, perfect for you."
)
inflatable_boat = FiniteUseThing(
    name='inflatable boat',
    description="Perfect for really hot days at the lake.",
    use_description="Your are using it...in the cellar, so it breaks.",
    status_descriptions=["This looks a bit fragile, be careful."],
    kills=False
)

donation_bags = Thing(
    name='donation bags',
    description="There are clothes, food and toiletries.",
)

tacky_dishes = InfiniteUseThing(
    name='tacky dishes',
    description="Not beautiful, but in one piece.",
    use_description="You may want to put some food on that first, but whatever. I'm not judging there."
)

box_of_chocolates = FiniteUseThing(
    name='box of chocolates',
    description="Not your thing, but you can use them to get your daughters to do what you want.",
    use_description="Mmm...delicious. Wait, what was the expiry date?",
    status_descriptions=["You don't know how to eat only one at a time."],
    kills=True
)

mailbox = Thing(
    name='mailbox',
    description="Just some bloody Werbung, not worth checking.",
)

shovel = InfiniteUseThing(
    name='shovel',
    description="Kid-size shovel. Perfect to dig in the sandbox.",
    use_description="Dig, dig...and a bit more dig."
)

flower_seeds = FiniteUseThing(
    name='flower seeds',
    description="Plant at the end of March, water and wait for the miracle to happen.",
    use_description="You planted the seeds, well done! But wait, are those flowers not poisonous?",
    status_descriptions=["Once you plant them they will be gone."],
    kills=True
)

swing = Thing(
    name='swing',
    description="You are too heavy for this, don't even dream about it.",
)

book = InfiniteUseThing(
    name='book',
    description="'Woman Rebel. The Margaret Sanger Story', by Peter Bagge.\nSounds cool, I wish I had the time to read it.",
    use_description="The life of the birth-control activist, educator, nurse, mother and protofeminist from her birth..."
)

friskies = FiniteUseThing(
    name='Friskies',
    description="Low-quality cat food. Exactly what your cat and you 2 year-old love to eat.",
    use_description="Crunch, crunch...yummy!",
    status_descriptions=["Go to dm later and get some more.", "There's still enough for the rest of the week.",
                         "It's full."],
    kills=True
)

window = Thing(
    name='window',
    description="You can see the tress blooming and some birds building a nest. Isn't spring wonderful?",
)

blanket = InfiniteUseThing(
    name='blanket',
    description="Not very clean, but soft and warm.",
    use_description="Mmm...that feels nice."
)

bubble_maker = FiniteUseThing(
    name='bubble-maker',
    description="'Catnip bubbles for stressed cats'...I'm wondering what it does to humans.",
    use_description="BLUB...BLUBB...BLUB...Yay!",
    status_descriptions=["Almost nothing left.", "Now there's only half of it left.", "It's full."],
    kills=True
)

cat = Thing(
    name='cat',
    description="That is a catosaur!",
)

hairbands = FiniteUseThing(
    name='hairbands',
    description="A bunch of colourful hairbands.",
    use_description="Yeah, I like not having hair on my face constantly.",
    status_descriptions=["These won't last forever.", "Enough for pigtails."],
    kills=False
)

phone = FiniteUseThing(
    name='phone',
    description="2435 unread emails, 3 likes on Instagram and way too many messages on the Elternchat on WhatsApp.",
    use_description="Let's check the weather for tomorrow...",
    status_descriptions=["It doesn't charge anymore.", "The screen is broken.", "Fully charged."],
    kills=False
)

litter_box = InfiniteUseThing(
    name='litter_box',
    description="It looks clean, thankfully, because you can see some hairbands fell in there and you should pick them up.",
    use_description="You removed some cat poo, all clean again."
)

knife = InfiniteUseThing(
    name='knife',
    description="It doesn't look very sharp, but it works.",
    use_description="zim zam zum"
)

mayo = FiniteUseThing(
    name='mayo',
    description="It doesn't look really fresh, but you're starving...",
    use_description="there you go, just a spoon full of...mayonnaise...",
    status_descriptions=["Expired.", "You can still have a few fries with it."],
    kills=True
)

table = Thing(
    name='table',
    description="This looks heavy.",
)

empty_beer_bottle = FiniteUseThing(
    name='empty beer bottle',
    description="An empty bottle of your favourite beer. You can use it to hit things.",
    use_description="Bang bang bang",
    status_descriptions=["Be careful, it's about to break.", "It's empty, but robust."],
    kills=True
)

bicycle = InfiniteUseThing(
    name='bicycle',
    description="A bit rusty, bit it works.",
    use_description="Ready to go."
)
chestnuts = FiniteUseThing(
    name='chestnuts',
    description="A handful of bitter chestnuts that your daughter loves to collect and store by the bathroom window.",
    use_description="Argghh, it was not a good idea to bite one of them.",
    status_descriptions=["You can hardly do anything with these.", "So many broken shells."],
    kills=True
)

rug = InfiniteUseThing(
    name='rug',
    description="Here is where all small things end up after passing the broom.",
    use_description="You lifted it up."
)
picture = Thing(
    name='picture',
    description="You could probably do that better. That's what Basquiat thought when he painted it.",
)
