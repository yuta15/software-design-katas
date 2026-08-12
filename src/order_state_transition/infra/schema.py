from enum import Enum
from uuid import UUID

from sqlmodel import Field, SQLModel


class OrderStatus(Enum):
    DRAFT = "DRAFT"
    PAID = "PAID"
    SHIPPED = "SHIPPED"
    CANCELED = "CANCELED"


class Order(SQLModel, table=True):
    __tablename__ = "orders"

    id: UUID = Field(primary_key=True)
    order_status: OrderStatus


class OrderItem(SQLModel, table=True):
    __tablename__ = "order_items"

    order_id: UUID = Field(foreign_key="orders.id", primary_key=True,)
    item_name: str = Field(primary_key=True)
    item_price: int
