class Engine:
    def engine(self):
        pass

    def start_engine(self):
        pass

class VehicleWithEngine(Engine):
    def __init__(self, name):
        self.name = name

    def engine(self):
        pass

    def start_engine(self):
        pass

class Car(VehicleWithEngine):
    def engine(self):
        """ define the engine """
        return True

    def start_engine(self):
        """ implement the start up process for the engine"""
        self.engine()

class Bike(VehicleWithEngine):
    def engine(self):
        """ define the engine """
        return True

    def start_engine(self):
        """ implement rest of the steps to start an engine"""
        self.engine()

class VehicleWithoutEngine:
    def __init__(self, name):
        self.name = name

    def start_pedaling(self):
        pass

class Bicycle(VehicleWithoutEngine):
    def start_pedaling(self):
        """implement the pedaling process"""
        return True

def drive_vehicle():
    car = Car('Queen')
    car.start_engine()

    bicycle = Bicycle('Booster')
    bicycle.start_pedaling()