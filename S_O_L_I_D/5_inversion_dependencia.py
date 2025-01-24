from abc import ABC, abstractmethod

"""
# High-level module
class NotificationService:
    def __init__(self, notifier):
        self.notifier = notifier

    def send(self, message):
        self.notifier.notify(message)

# Low-level module
class EmailNotifier:
    def notify(self, message):
        print(f"Sending email with message: {message}")

class SMSNotifier:
    def notify(self, message):
        print(f"Sending SMS with message: {message}")

# Dependency inversion principle in action
if __name__ == "__main__":
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()

    notification_service = NotificationService(email_notifier)
    notification_service.send("Hello via Email!")

    notification_service = NotificationService(sms_notifier)
    notification_service.send("Hello via SMS!")
"""

"""
Explicación:
El principio de inversión de dependencia (DIP) establece que los módulos de alto nivel no deben depender de módulos de bajo nivel, sino de abstracciones. En este ejemplo, `NotificationService` es un módulo de alto nivel que depende de una abstracción (la interfaz `Notifier`) en lugar de depender directamente de implementaciones concretas como `EmailNotifier` o `SMSNotifier`. Esto permite que `NotificationService` sea independiente de las implementaciones específicas de notificación y facilita la extensión y el mantenimiento del código.
"""

# Otro ejemplo del principio de inversión de dependencia

# Interfaz abstracta
class Notifier(ABC):
    @abstractmethod
    def notify(self, message):
        pass

# Módulo de alto nivel
class OrderProcessor:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def process_order(self, order_id):
        # Lógica para procesar la orden
        print(f"Processing order {order_id}")
        self.notifier.notify(f"Order {order_id} has been processed")

# Módulos de bajo nivel
class EmailNotifier(Notifier):
    def notify(self, message):
        print(f"Sending email with message: {message}")

class SMSNotifier(Notifier):
    def notify(self, message):
        print(f"Sending SMS with message: {message}")

# Uso del principio de inversión de dependencia
if __name__ == "__main__":
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()

    order_processor = OrderProcessor(email_notifier)
    order_processor.process_order(1)

    order_processor = OrderProcessor(sms_notifier)
    order_processor.process_order(2)
