from uuid import UUID

from ...domain import ItemNameVo, OrderItem, PriceVo
from ..ports import OrderRepositoryPort


class AddItems:
    def __init__(self, repository: OrderRepositoryPort):
        self._repository = repository

    def exec(self, order_id: UUID, item_name: str, item_price: int) -> None:
        order = self._repository.get(order_id=order_id)
        order.add_item(OrderItem(item_name=ItemNameVo(value=item_name), item_price=PriceVo(value=item_price)))
        print(order.price)
        self._repository.save(order=order)
