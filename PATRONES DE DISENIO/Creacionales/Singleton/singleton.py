class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)

        return cls._instances[cls]
    
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)

import sqlite3

class DatabaseConnection(Singleton):
    connection = None

    def __init__(self):
        if self.connection is None:
            self.connection = sqlite3.connect("users.db")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users (name) VALUES ('Alina')")

db3 = DatabaseConnection()
db3.execute_query("INSERT INTO users (name) VALUES ('Leonor')")

print(db1 is db2)

<<<<<<< HEAD:PATRONES DE DISENIO/Singleton/singleton.py
db1.close()
db2.close()
db3.close()
=======
db1.close() 
db2.close()
db3.close()
>>>>>>> 92cc72c0a43f0da16ceccc72fbf15bd6f542c522:PATRONES DE DISENIO/singleton.py
