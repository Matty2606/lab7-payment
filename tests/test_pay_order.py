import pytest
from domain.order import Order, OrderLine, Money
from application.pay_order_usecase import PayOrderUseCase
from infrastructure.in_memory_order_repository import InMemoryOrderRepository
from infrastructure.fake_payment_gateway import FakePaymentGateway

def create_sample_order(order_id='1', empty=False):
    lines = [] if empty else [OrderLine('p1', 2, Money(50))]
    return Order(order_id, lines)

def test_successful_payment():
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()
    order = create_sample_order()
    repo.save(order)
    usecase = PayOrderUseCase(repo, gateway)
    result = usecase.execute(order.order_id)
    assert result['status'] == 'paid'
    assert result['total'] == 100
    assert gateway.charges == [('1', 100)]

def test_empty_order_payment():
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()
    order = create_sample_order(empty=True)
    repo.save(order)
    usecase = PayOrderUseCase(repo, gateway)
    with pytest.raises(ValueError):
        usecase.execute(order.order_id)

def test_double_payment():
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()
    order = create_sample_order()
    repo.save(order)
    usecase = PayOrderUseCase(repo, gateway)
    usecase.execute(order.order_id)
    with pytest.raises(ValueError):
        usecase.execute(order.order_id)

def test_order_immutable_after_payment():
    order = create_sample_order()
    order.pay()
    with pytest.raises(AttributeError):
        order.lines.append(OrderLine('p2',1,Money(10)))

def test_total_calculation():
    order = create_sample_order()
    assert order.total.amount == 100
