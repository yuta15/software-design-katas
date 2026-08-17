import datetime
from uuid import UUID, uuid7

from ..value_objects import AmountVo, ExpenseNameVo


class Usage:
    def __init__(
        self, id_: UUID, customer_id: UUID, expense_name: ExpenseNameVo, amount: AmountVo, usage_date: datetime.date
    ):
        self._id: UUID = id_
        self._customer_id: UUID = customer_id
        self._expense_name: ExpenseNameVo = expense_name
        self._amount: AmountVo = amount
        self._usage_date: datetime.date = usage_date

    @property
    def id_(self) -> UUID:
        return self._id

    @property
    def customer_id(self) -> UUID:
        return self._customer_id

    @property
    def expense_name(self) -> ExpenseNameVo:
        return self._expense_name

    @property
    def amount(self) -> AmountVo:
        return self._amount

    @property
    def usage_date(self) -> datetime.date:
        return self.usage_date

    @classmethod
    def new(cls, customer_id: UUID, expense_name: ExpenseNameVo, amount: AmountVo, usage_date: datetime.date) -> Usage:
        return cls(
            id_=uuid7(), customer_id=customer_id, expense_name=expense_name, amount=amount, usage_date=usage_date
        )

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Usage):
            if self._id == value.id_ and self._customer_id == value._customer_id:
                return True
        return False
