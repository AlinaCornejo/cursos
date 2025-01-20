from component import FileSystemComponent

class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, child):
        self.children.append(child)

    def show_details(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.show_details()