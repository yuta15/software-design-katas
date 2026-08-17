from abc import ABC, abstractmethod

from .models import BillingData


class BillingReadRepository(ABC):
    @abstractmethod
    def list_billing_data(self) -> tuple[BillingData]: ...
