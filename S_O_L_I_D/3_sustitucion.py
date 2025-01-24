"""
Este programa demuestra el Principio de Sustitución de Liskov (Liskov Substitution Principle, LSP)
mediante la implementación de clases de vehículos con y sin motor.
Clases:
    Engine: Clase base abstracta que define la interfaz para un motor.
    VehicleWithEngine: Clase base que hereda de Engine y representa un vehículo con motor.
    Car: Subclase de VehicleWithEngine que implementa los métodos para un coche.
    Bike: Subclase de VehicleWithEngine que implementa los métodos para una motocicleta.
    VehicleWithoutEngine: Clase base que representa un vehículo sin motor.
    Bicycle: Subclase de VehicleWithoutEngine que implementa los métodos para una bicicleta.
Funciones:
    drive_vehicle: Función que crea instancias de Car y Bicycle y llama a sus métodos para iniciar el motor 
    o comenzar a pedalear.
El programa demuestra cómo las subclases pueden reemplazar a sus superclases sin afectar el comportamiento 
del programa, cumpliendo así con el Principio de Sustitución de Liskov.

## ------------------------------------------------
Principio de sustitución de Liskov

El principio de sustitución de Liskov es un principio de diseño de clases que establece que los objetos de una superclase
deben poder ser reemplazados por objetos de sus subclases sin afectar la integridad del programa.

En otras palabras, si una clase A es una subclase de una clase B, entonces los objetos de la clase B pueden ser reemplazados
por objetos de la clase A sin afectar el comportamiento del programa.

Este principio es importante porque garantiza que las subclases sean compatibles con las superclases y que puedan ser usadas
en lugar de las superclases sin problemas.

Ejemplo:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height    

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

        
rect = Rectangle(2, 3)
print(rect.area())  # Output: 6

square = Square(2)
print(square.area())  # Output: 4

En este ejemplo, la clase Square es una subclase de la clase Rectangle. La clase Square tiene un método __init__ que inicializa
el lado del cuadrado y sobrescribe el método area de la clase Rectangle para calcular el área del cuadrado.

El principio de sustitución de Liskov se cumple en este ejemplo porque los objetos de la clase Square pueden ser reemplazados
por objetos de la clase Rectangle sin afectar el comportamiento del programa.

En resumen, el principio de sustitución de Liskov es un principio de diseño de clases que garantiza que las subclases sean
compatibles con las superclases y puedan ser usadas en lugar de las superclases sin problemas.

    """

class Engine:
    def engine(self):
        pass

    def start_engine(self):
        pass

class VehicleWithEngine(Engine):
    def __init__(self, name):
        self.name = name
        print("CAR.. Engine started") 

    def engine(self):
        pass

    def start_engine(self):
        pass

class Car(VehicleWithEngine):
    def engine(self):
        """ define the engine """
        print("CAR.. Engine started") 
        return True

    def start_engine(self):
        """ implement the start up process for the engine"""
        print("CAR .. Starting the engine")
        self.engine()

class Bike(VehicleWithEngine):
    def engine(self):
        """ define the engine """
        print("Bike.. Engine started")
        return True

    def start_engine(self):
        """ implement rest of the steps to start an engine"""
        print("Bike.. Starting the engine")
        self.engine()


class VehicleWithoutEngine:
    def __init__(self, name):
        self.name = name
        print("Vehicle without engine")

    def start_pedaling(self):
        pass

class Bicycle(VehicleWithoutEngine):
    def start_pedaling(self):
        """implement the pedaling process"""
        print("Bike .. Start pedaling")
        return True
    

def drive_vehicle():
    
    car = Car('Queen')
    car.start_engine()

    bicycle = Bicycle('Booster')
    bicycle.start_pedaling()

"""     car = VehicleWithEngine('Queen')
    car.start_engine()

    bicycle = VehicleWithoutEngine('Booster')
    bicycle.start_pedaling() """

if __name__ == '__main__': 
    drive_vehicle()

