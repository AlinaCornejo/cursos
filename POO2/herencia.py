class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau"
    
class Gato(Animal):
    def sonido(self):
        return "Miau"
    
perro = Perro("Loki")
gato = Gato('Vaquita')

print(perro.nombre, "dice", perro.sonido())
print(gato.nombre, "dice", gato.sonido())