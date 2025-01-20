class ChessPieceFlyweight:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def display(self, position):
        print(f"Displaying {self.name} ({self.color} at {position})")