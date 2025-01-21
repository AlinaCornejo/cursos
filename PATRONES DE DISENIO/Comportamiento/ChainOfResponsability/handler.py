from abc import ABC, abstractmethod

class SupportHandler(ABC):
    def __init__(self, next_handler):
        self._next_handler = next_handler

    @abstractmethod
    def handle_request(self, request):
        pass

class LevelOneSupportHandle(SupportHandler):
    def handle_request(self, request):
        if request.level == 1:
            print("Level one support has resolved the issue")
        else:
            self._next_handler.handle_request(request)

class LevelTwoSupportHandle(SupportHandler):
    def handle_request(self, request):
        if request.level == 2:
            print("Level two support has resolved the issue")
        else:
            self._next_handler.handle_request(request)