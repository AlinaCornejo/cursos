from abc import ABC, abstractmethod
from vehicle_factory.product import Car, Truck

class VehicleFactory(ABC):
    @abstractmethod
    def get_vehicle(self, vehicle_type):
        pass
