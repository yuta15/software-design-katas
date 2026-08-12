from uuid import UUID
from abc import ABC, abstractmethod

from ...domain.entities import Order


class OrderRepositoryPort(ABC):
    @abstractmethod
    def get(self, order_id:UUID) -> Order:...

    @abstractmethod
    def save(self, order:Order) -> Order:...
