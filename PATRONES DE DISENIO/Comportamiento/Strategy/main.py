from strategy import FixedCommission, PercentageCommission
from context import PaymentProcessor

def main():
    processor = PaymentProcessor(FixedCommission())
    print(processor.process_payment(100))

    processor = PaymentProcessor(PercentageCommission())
    print(processor.process_payment(100))

if __name__ == "__main__":
    main()