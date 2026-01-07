class InMemoryOrderRepository:
    def __init__(self):
        self.store = {}

    def get_by_id(self, order_id: str):
        if order_id not in self.store:
            raise ValueError('Order not found')
        return self.store[order_id]

    def save(self, order):
        self.store[order.order_id] = order
