"""
Principio abierto-cerrado
Los objetos o entidades (clases, módulos, funciones) deben estar abiertos a la extensión, no a la modificación.    

class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        pass

def animal_sounds(animals):
    for animal in animals:
        if animal.name == "lion":
            print("roar")
        elif animal.name == "mouse":
            print("squeak")

animals = [
    Animal("lion"),
    Animal("mouse")
]

animal_sounds(animals)

Problema: Si se agrega un nuevo animal, se debe modificar la función animal_sounds.
Solución: Crear una clase base Animal y extenderla para cada
animal concreto. Así, se puede agregar un nuevo animal sin modificar la función animal_sounds.

"""

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

class Perro(Animal):
    def make_sound(self):
        print("guau")

class Gato(Animal):
    def make_sound(self):
        print("miau")

class Gallo(Animal):
    def make_sound(self):
        print("pio")

class Cow(Animal):
    def make_sound(self):
        print("moo")

class Tigre(Animal):
    def make_sound(self):
        print("grrr")   

def animal_sounds(animals):
    for animal in animals:
        animal.make_sound()

animals = [
    Lion(name="Big Cat"),
    Mouse(name="Squeakie"),
    Perro(name="Firulais"),
    Gato(name="Mishi"),   
    Gallo(name="Pio"),
    Cow(name="Moo"),
    Tigre(name="Tigre"),
]

animal_sounds(animals)
