class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("roar")

class Mouse(Animal):
    def make_sound(self):
        print("squeak")

class Cow(Animal):
    def make_sound(self):
        print("moo")

def animal_sounds(animals):
    for animal in animals:
        animal.make_sound()

animals = [
    Lion(name="Big Cat"),
    Mouse(name="Squeakie")
]

animal_sounds(animals)