from uuid import UUID

from sqlalchemy.orm import selectinload
from sqlmodel import Session, select, delete, exists

from ..application import OrderRepositoryPort
from ..domain import Order, Draft, Shipped, Canceled, Paid, OrderStatus, OrderItem, ItemNameVo, PriceVo
from .schema import Order as db_orders
from .schema import OrderItem as db_order_items
from .schema import OrderStatus as db_order_status


class OrderRepository(OrderRepositoryPort):
    def __init__(self, session:Session):
        self._session = session

    def save(self, order:Order) -> None:
        order_status = self._resolve_db_order_status(order.order_status)
        if not self._exists(order.id):
            self._session.add(db_orders(id=order.id, order_status=order_status))
            items = []
            for order_item in order.order_items:
                items.append(db_order_items(order_id=order.id, item_name=order_item.item_name.value, item_price=order_item.item_price.value))
            self._session.add_all(items)
        else:
            db_order = self._get_db_orders(order.id)
            db_order.order_status = self._resolve_db_order_status(order.order_status)
            self._session.exec(delete(db_order_items).where(db_order_items.order_id == order.id))

            append_items = []
            for item in order.order_items:
                append_items.append(db_order_items(order_id=order.id, item_name=item.item_name.value, item_price=item.item_price.value))
            self._session.add_all(append_items)

    def get(self, order_id:UUID) -> Order:
        db_order = self._get_db_orders(order_id)
        db_order_items = self._get_db_items(order_id)
        return self._build_order(db_order, db_order_items)

    def _exists(self, order_id:UUID) -> bool:
        statement = select(exists().where(db_orders.id == order_id))
        return self._session.exec(statement).one()

    def _get_db_orders(self, order_id:UUID) -> db_orders:
        return self._session.get(db_orders, order_id)

    def _get_db_items(self, order_id:UUID) -> list[db_order_items]:
        return self._session.exec(select(db_order_items).where(db_order_items.order_id == order_id)).all()

    def _resolve_db_order_status(self, order_status:OrderStatus) -> db_order_status:
        mapping = {
            Draft: db_order_status.DRAFT,
            Shipped: db_order_status.SHIPPED,
            Paid: db_order_status.PAID,
            Canceled: db_order_status.CANCELED
        }
        return mapping[type(order_status)]

    def _resolve_order_status(self, db_order_status:db_order_status) -> OrderStatus:
        mapping = {
            db_order_status.DRAFT:Draft,
            db_order_status.SHIPPED:Shipped,
            db_order_status.PAID:Paid,
            db_order_status.CANCELED:Canceled
        }
        return mapping[db_order_status]()

    def _build_order(self, db_order:db_orders, db_order_items:list[db_order_items]) -> Order:
        order_items = []
        for db_order_item in db_order_items:
            order_items.append(
                OrderItem(item_name=ItemNameVo(db_order_item.item_name), item_price=PriceVo(db_order_item.item_price))
                )
        return Order.reconstruct(id=db_order.id, order_items=order_items, order_status=self._resolve_order_status(db_order.order_status))