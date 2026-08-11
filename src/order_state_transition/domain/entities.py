from abc import abstractmethod, ABC
from datetime import datetime, timezone
from uuid import UUID

from .value_objects import ItemNameVo, PriceVo


class Order:
    def __init__(self, *, id, order_items:list[OrderItem], price:PriceVo, order_status:OrderStatus):
        self._id = id
        self._order_items:list[OrderItem] = order_items
        self._price:PriceVo = price
        self._order_status:OrderStatus = order_status

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def order_items(self) -> list[OrderItem]:
        return self._order_items

    @property
    def price(self) -> PriceVo:
        return self._price

    @property
    def order_status(self) -> OrderStatus:
        return self._order_status

    def __setattr__(self, name, value):
        if name == "_id" and getattr(self, "_id", None) is not None:
            raise AttributeError("Change entity ID is not permitted")
        object.__setattr__(name, value)

    def __eq__(self, value:object) -> bool:
        if isinstance(value, Order):
            return value.id == self._id
        return False

    def __hash__(self):
        return hash(self._id)

    def add_item(self, item:OrderItem) -> None:
        if not isinstance(item, OrderItem):
            raise AttributeError("Invalid item value")
        new_items = [*self._order_items, item]
        new_price = self._price.value + item.item_price.value
        self._order_items = new_items
        self._price = PriceVo(value=new_price)

    def remove_item(self, item:OrderItem) -> None:
        if not isinstance(item, OrderItem):
            raise AttributeError("Invalid item value")

        if not item in self.order_items:
            raise AttributeError("Not include specified item")

        new_items = []
        for exist_item in self._order_items:
            if exist_item != item:
                new_items.append(exist_item)

        new_price = self._price.value - item.item_price.value

        self._order_items = new_items
        self._price = PriceVo(value=new_price)

    def pay(self) -> None:
        self._order_status.pay()

    def cancel(self) -> None:
        self._order_status.cancel()

    def ship(self) -> None:
        self._order_status.ship()


class OrderItem:
    def __init__(self, *, item_name:ItemNameVo, item_price:PriceVo):
        self._item_name: ItemNameVo = item_name
        self._item_price: PriceVo = item_price

    @property
    def item_name(self) -> ItemNameVo:
        return self._item_name

    @property
    def item_price(self) -> PriceVo:
        return self._item_price


class OrderStatus(ABC):
    def __init__(self):
        self._changed_at = datetime.now(timezone.utc)

    @property
    def changed_at(self) -> datetime:
        return self._changed_at

    @abstractmethod
    def pay(self) -> OrderStatus:...

    @abstractmethod
    def cancel(self) -> OrderStatus:...

    @abstractmethod
    def ship(self) -> OrderStatus:...


class Canceled(OrderStatus):
    def pay(self):
        raise RuntimeError("invalid operation")

    def cancel(self):
        raise RuntimeError("already canceled")

    def ship(self):
        raise RuntimeError("already canceled")


class Shipped(OrderStatus):
    def pay(self):
        raise RuntimeError("Already shipped")

    def cancel(self):
        raise RuntimeError("Already shipped")

    def ship(self):
        raise RuntimeError("Already shipped")


class Paid(OrderStatus):
    def pay(self):
        raise RuntimeError("Already paid")

    def cancel(self):
        raise RuntimeError("Already paid")

    def ship(self):
        return Shipped()


class Draft(OrderStatus):
    def pay(self):
        return Paid()

    def ship(self):
        raise RuntimeError("not paid")

    def cancel(self):
        return Canceled()
        