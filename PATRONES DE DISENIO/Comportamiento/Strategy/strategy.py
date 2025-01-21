from abc import ABC, abstractmethod

class CommissionStrategy(ABC):
    @abstractmethod
    def calculate_commission(self, amount):
        pass

class FixedCommission(CommissionStrategy):
    def calculate_commission(self, amount):
        return 5
    
class PercentageCommission(CommissionStrategy):
    def calculate_commission(self, amount):
        return amount * 0.05