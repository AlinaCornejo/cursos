from vehicle_factory.client_code import client_vehicle_code
from vehicle_factory.concrete_factory import CarFactory, TruckFactory

if __name__ == "__main__":
    client_vehicle_code(CarFactory(), "SEDAN")
    client_vehicle_code(TruckFactory(), "REMOLQUE")