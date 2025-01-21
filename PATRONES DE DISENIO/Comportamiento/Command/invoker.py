class Button:
    def __init__(self, command):
        self.command = command

    def press(self):
        self.command.execute()