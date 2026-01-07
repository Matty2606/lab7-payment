class FakePaymentGateway:
    def __init__(self):
        self.charges = []

    def charge(self, order_id: str, money):
        self.charges.append((order_id, money.amount))
