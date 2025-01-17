import copy
from prototype import Prototype

class SystemConfigPrototype(Prototype):
    def __init__(self, configuration):
        self.configuration = configuration

    def clone(self):
        return copy.deepcopy(self)        