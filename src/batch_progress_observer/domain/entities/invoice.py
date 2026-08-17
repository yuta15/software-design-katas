from uuid import UUID, uuid7

from ..value_objects import AmountVo, YearMonthVo


class Invoice:
    def __init__(self, id_: UUID, customer_id: UUID, invoice_month: YearMonthVo, month_amount: AmountVo):
        self._id: UUID = id_
        self._customer_id: UUID = customer_id
        self._invoice_month: YearMonthVo = invoice_month
        self._month_amount: AmountVo = month_amount

    @property
    def id_(self) -> UUID:
        return self._id

    @property
    def customer_id(self) -> UUID:
        return self._customer_id

    @property
    def invoice_month(self) -> YearMonthVo:
        return self._invoice_month

    @property
    def month_amount(self) -> AmountVo:
        return self._month_amount

    @classmethod
    def new(cls, customer_id: UUID, invoice_month: YearMonthVo, month_amount: AmountVo) -> Invoice:
        return cls(id_=uuid7(), customer_id=customer_id, invoice_month=invoice_month, month_amount=month_amount)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Invoice):
            if all(
                [
                    self._id == value.id_,
                    self.customer_id == value.customer_id,
                    self.invoice_month == value.invoice_month,
                ]
            ):
                return True
        return False
