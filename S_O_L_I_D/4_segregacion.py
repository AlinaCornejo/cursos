
""""
El principio de segregación de interfaces (Interface Segregation Principle, ISP) es uno de los
 principios SOLID de la programación orientada a objetos. Este principio establece que una clase
 no debería estar obligada a implementar interfaces que no utiliza. En otras palabras, 
 es mejor tener varias interfaces específicas y pequeñas en lugar de una única interfaz
 grande y general.

A continuación, te muestro un ejemplo en Python para ilustrar este principio:

"""

from abc import ABC, abstractmethod

# Definimos interfaces específicas y pequeñas
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Nadador(ABC):
    @abstractmethod
    def nadar(self):
        pass

# Ahora, la clase Perro solo implementará la interfaz Comedor
class Perro(Comedor):
    def comer(self):
        print("El perro está comiendo")

# La clase Pajaro implementará las interfaces Comedor y Volador
class Pajaro(Comedor, Volador):
    def comer(self):
        print("El pájaro está comiendo")

    def volar(self):
        print("El pájaro está volando")

# La clase Pez implementará las interfaces Comedor y Nadador
class Pez(Comedor, Nadador):
    def comer(self):
        print("El pez está comiendo")

    def nadar(self):
        print("El pez está nadando")

# Uso del principio de segregación de interfaces
if __name__ == "__main__":
    perro = Perro()
    perro.comer()

    pajaro = Pajaro()
    pajaro.comer()
    pajaro.volar()

    pez = Pez()
    pez.comer()
    pez.nadar()

""""
En este ejemplo:

Comedor, Volador y Nadador son interfaces específicas y pequeñas que definen métodos individuales.
Perro implementa solo la interfaz Comedor porque solo necesita el método comer.
Pajaro implementa las interfaces Comedor y Volador porque necesita los métodos comer y volar.
Pez implementa las interfaces Comedor y Nadador porque necesita los métodos comer y nadar.

De esta manera, cada clase solo implementa los métodos que realmente necesita, cumpliendo con el 
principio de segregación de interfaces. Esto hace que el código sea más limpio, más fácil 
de mantener y menos propenso a errores.

Para utilizar este ejemplo, simplemente ejecuta el script. Verás que cada clase 
realiza las acciones correspondientes a los métodos que ha implementado.

"""