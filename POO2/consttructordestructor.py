class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Objeto {self.nombre} creado")

    def __del__(self):
        print(f"Objecto {self.nombre} destruido")

def mi_funcion():
    obj_f = MiClase("F")
    del obj_f

obj_a = MiClase("A")
mi_funcion( )
obj_b = MiClase("B")
obj_c = MiClase("C")
obj_d = MiClase("D")