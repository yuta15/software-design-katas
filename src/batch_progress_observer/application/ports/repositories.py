from abc import ABC, abstractmethod
from uuid import UUID

from ...domain.entities import Customer, Invoice, Usage


class CustomerRepositoryPort(ABC):
    @abstractmethod
    def get(self, customer_id: UUID) -> Customer: ...

    @abstractmethod
    def save(self, customer: Customer) -> None: ...


class UsageRepositoryPort(ABC):
    @abstractmethod
    def get(self, usage_id: UUID) -> Usage: ...

    @abstractmethod
    def save(self, usage: Usage) -> None: ...


class InvoiceRepositoryPort(ABC):
    @abstractmethod
    def get(self, invoice_id: UUID) -> Invoice: ...

    @abstractmethod
    def save(self, invoice: Invoice) -> None: ...
