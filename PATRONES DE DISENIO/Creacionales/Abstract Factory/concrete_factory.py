from abstract_factory import UIAbstractFactory, Button, TextBox

class DarkButton(Button):
    def paint(self):
        print("Dark Button")

class DarkTextBox(TextBox):
    def paint(self):
        print("Dark TextBox")

class LightButton(Button):
    def paint(self):
        print("Light Button")

class LightTextBox(TextBox):
    def paint(self):
        print("Light TextBox")

class DarkUIFactory(UIAbstractFactory):
    def create_button(self):
        return DarkButton()
    
    def create_textbox(self):
        return DarkTextBox()
    
class LightUIFactory(UIAbstractFactory):
    def create_button(self):
        return LightButton()
    
    def create_textbox(self):
        return LightTextBox()