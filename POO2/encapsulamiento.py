
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre 
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    

    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser positiva")


personas = Persona(nombre= 'Romina', edad= 30 )
print(personas.get_nombre())
personas.set_nombre("Leonor")
print(personas.get_nombre())

personas.set_edad(1)
print(personas.get_edad())