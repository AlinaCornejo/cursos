class Payment:
    def process_payment(self, user_id, amount):
        print(f'User: {user_id} paid ${amount}')
        return True