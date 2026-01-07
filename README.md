laba 7

Проделанные изменения
- Слои: Domain, Application, Infrastructure, Tests
- Domain: Order, OrderLine, Money, OrderStatus, инварианты
- Application: PayOrderUseCase
- Infrastructure: InMemoryOrderRepository, FakePaymentGateway
- Tests: проверка успешной оплаты, ошибок на пустой и повторной оплате, неизменяемости и расчета суммы
