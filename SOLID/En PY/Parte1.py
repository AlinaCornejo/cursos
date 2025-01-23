class AnimalDB:
    def save(self, animal):
        """Saves the animal details to DB"""
        pass

    def get_animal(self, _id):
        """Gets the animal details by _id from the DB"""
        pass

class Animal:
    def __init__(self, name):
        self.name = name
        self._db = AnimalDB()

    def get_name(self):
        """Get animal name"""
        return self.name

    def save(self):
        """Saves the animal to DB"""
        self._db.save(animal=self)