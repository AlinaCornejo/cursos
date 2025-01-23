class Database:

    def insert(self, data):
        pass

    def delete(self, id):
        pass

class MySQLDatabase(Database):

    def insert(self, data):
        """Logic to save the data in MySQL DB"""
        pass

    def delete(self, id):
        """Logic to delete a row from the MySQL DB"""
        pass


class CarManufacturer():
    def __init__(self, DB: Database):
        self._db = DB

    def create_car(self, data):
        self._db.insert(data)

    def delete_car(self, car_id):
        self._db.delete(car_id)