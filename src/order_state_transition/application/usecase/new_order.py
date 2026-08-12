from uuid import uuid7
from ..ports import OrderRepositoryPort
from ...domain import Order


class NewOrder:
    def __init__(self, repository:OrderRepositoryPort):
        self._repository = repository

    def exec(self) -> None:
        order_id = uuid7()
        order = Order.create(id=order_id)
        self._repository.save(order=order)
