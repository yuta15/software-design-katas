from uuid import uuid7

from ...domain import Order
from ..ports import OrderRepositoryPort


class NewOrder:
    def __init__(self, repository: OrderRepositoryPort):
        self._repository = repository

    def exec(self) -> None:
        order_id = uuid7()
        order = Order.create(id=order_id)
        self._repository.save(order=order)
