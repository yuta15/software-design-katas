from dataclasses import dataclass
from enum import Enum
from uuid import UUID

from ...domain.entities import Invoice, Usage


@dataclass(frozen=True, slots=True)
class BillingData:
    customer_id: UUID
    usages: tuple[Usage]
    invoice: Invoice


class Result(Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


@dataclass(frozen=True, slots=True)
class NotifyData:
    current_customers_number: int
    total_customers_number: int
    customer_id: UUID
    customer_name: str
    result: Result
    message: str
