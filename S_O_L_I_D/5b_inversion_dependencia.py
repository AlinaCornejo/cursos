""""
Claro, el principio de inversión de dependencia (DIP) es uno de los principios SOLID de diseño de software. 
Este principio establece que:

Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.
Las abstracciones no deben depender de detalles. Los detalles deben depender de abstracciones.

En otras palabras, el código debe depender de interfaces o abstracciones en lugar de implementaciones concretas.
 Esto hace que el código sea más flexible y fácil de mantener.

A continuación, te muestro un ejemplo en Python para ilustrar este principio:

En este ejemplo:

Notificador es una abstracción (interfaz) que define el método enviar.
NotificadorEmail y NotificadorSMS son implementaciones concretas de la interfaz Notificador.
GestorDeAlertas es una clase de alto nivel que depende de la abstracción Notificador en lugar de
depender directamente de NotificadorEmail o NotificadorSMS.
Esto permite que GestorDeAlertas sea flexible y pueda trabajar con cualquier implementación 
de Notificador sin necesidad de cambios en su código.

"""

# Definimos una abstracción (interfaz) para un servicio de notificación
class Notificador:
    def enviar(self, mensaje: str):
        pass

# Implementación concreta del servicio de notificación por correo electrónico
class NotificadorEmail(Notificador):
    def enviar(self, mensaje: str):
        print(f"Enviando correo electrónico: {mensaje}")

# Implementación concreta del servicio de notificación por SMS
class NotificadorSMS(Notificador):
    def enviar(self, mensaje: str):
        print(f"Enviando SMS: {mensaje}")

# Clase de alto nivel que depende de la abstracción Notificador
class GestorDeAlertas:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador

    def enviar_alerta(self, mensaje: str):
        self.notificador.enviar(mensaje)

# Uso del principio de inversión de dependencia
if __name__ == "__main__":
    # Podemos cambiar fácilmente la implementación del notificador sin cambiar la clase GestorDeAlertas
    notificador_email = NotificadorEmail()
    gestor_alertas_email = GestorDeAlertas(notificador_email)
    gestor_alertas_email.enviar_alerta("Alerta de prueba por correo electrónico")

    notificador_sms = NotificadorSMS()
    gestor_alertas_sms = GestorDeAlertas(notificador_sms)
    gestor_alertas_sms.enviar_alerta("Alerta de prueba por SMS")

