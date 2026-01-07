class PayOrderUseCase:
    def __init__(self, order_repo, payment_gateway):
        self.order_repo = order_repo
        self.payment_gateway = payment_gateway

    def execute(self, order_id: str):
        order = self.order_repo.get_by_id(order_id)
        order.pay()
        self.payment_gateway.charge(order.order_id, order.total)
        self.order_repo.save(order)
        return { 'order_id': order.order_id, 'status': order.status.value, 'total': order.total.amount }
