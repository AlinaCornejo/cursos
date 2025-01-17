from vehicle_factory.creator import VehicleFactory
from vehicle_factory.product import Car, Truck

class CarFactory(VehicleFactory):
    def get_vehicle(self, vehicle_type):
        return Car(vehicle_type)
    
class TruckFactory(VehicleFactory):
    def get_vehicle(self, vehicle_type):
        return Truck(vehicle_type)
    
