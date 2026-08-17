from enum import Enum
from uuid import UUID

from ..ports import OrderRepositoryPort


class Operation(Enum):
    PAY = "PAY"
    CANCEL = "CANCEL"
    SHIP = "SHIP"


class ChangeOrderState:
    def __init__(self, repository: OrderRepositoryPort):
        self._repository = repository

    def exec(self, order_id: UUID, operation_str: str) -> None:
        operation = Operation(operation_str)
        order = self._repository.get(order_id=order_id)
        if operation == Operation.PAY:
            order.pay()
        elif operation == Operation.SHIP:
            order.ship()
        elif operation == Operation.CANCEL:
            order.cancel()
        self._repository.save(order=order)
