from uuid import UUID

from ..entities import Invoice, Usage
from ..value_objects import AmountVo, YearMonthVo


class InvoiceService:
    def create_invoice(
        self,
        customer_id: UUID,
        target_year_month: YearMonthVo,
        target_month_usages: tuple[Usage],
        target_month_invoice: Invoice | None = None,
    ) -> Invoice | None:
        if target_month_invoice is None:
            return None

        target_usages = self._select_target_usage(target_year_month, target_month_usages)
        amount = self._to_month_amount(target_usages)
        return Invoice.new(customer_id=customer_id, invoice_month=target_year_month, month_amount=amount)

    def _select_target_usage(self, year_month: YearMonthVo, target_month_usages: tuple[Usage]) -> list[Usage]:
        target_usages = []
        for target_month_usage in target_month_usages:
            year = target_month_usage.usage_date.year
            month = target_month_usage.usage_date.month
            if year == year_month.year and month == year_month.month:
                target_usages.append(target_month_usage)
        return target_usages

    def _to_month_amount(self, usages: list[Usage]) -> AmountVo:
        amount = 0
        for usage in usages:
            amount += usage.amount.value
        return AmountVo(value=amount)
