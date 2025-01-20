from decorator import TextDecorator

class HTMLDecorator(TextDecorator):
    def render(self):
        return f'<HTML>{self._text_component.render()}</HTML>'