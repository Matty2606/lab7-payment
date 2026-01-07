from enum import Enum

class OrderStatus(Enum):
    PENDING = 'pending'
    PAID = 'paid'

class Money:
    def __init__(self, amount: int):
        if amount < 0:
            raise ValueError('Amount must be non-negative')
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __repr__(self):
        return f'Money({self.amount})'

class OrderLine:
    def __init__(self, product_id: str, quantity: int, price: Money):
        if quantity <= 0:
            raise ValueError('Quantity must be positive')
        if price.amount <= 0:
            raise ValueError('Price must be positive')
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    @property
    def total(self):
        return Money(self.quantity * self.price.amount)

class Order:
    def __init__(self, order_id: str, lines: list[OrderLine]):
        self.order_id = order_id
        self._lines = list(lines)
        self.status = OrderStatus.PENDING

    @property
    def lines(self):
        return tuple(self._lines)

    @property
    def total(self):
        total = Money(0)
        for line in self._lines:
            total += line.total
        return total

    def pay(self):
        if not self._lines:
            raise ValueError('Cannot pay empty order')
        if self.status == OrderStatus.PAID:
            raise ValueError('Order already paid')
        self.status = OrderStatus.PAID
