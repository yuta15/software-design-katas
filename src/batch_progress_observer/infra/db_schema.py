from datetime import date
from uuid import UUID

from sqlmodel import CheckConstraint, Field, SQLModel, UniqueConstraint


class Customers(SQLModel, table=True):
    id: UUID = Field(primary_key=True)
    name: str = Field(min_length=0, max_length=128, nullable=False)
    email: str = Field(min_length=0, nullable=False)


class Usages(SQLModel, table=True):
    __table_args__ = (CheckConstraint("amount >= 0", name="ck_usages_amount"),)

    id: UUID = Field(primary_key=True)
    customer_id: UUID = Field(index=True, nullable=False, foreign_key="customers.id")
    expense_name: str = Field(nullable=False)
    amount: int = Field(ge=0, nullable=False)
    usage_date: date = Field(nullable=False)


class Invoice(SQLModel, table=True):
    __table_args__ = (
        CheckConstraint("month BETWEEN 1 AND 12"),
        UniqueConstraint(
            "customer_id",
            "year",
            "month",
            name="uq_invoice_customer_year_month",
        ),
    )

    id: UUID = Field(primary_key=True)
    customer_id: UUID = Field(index=True, nullable=False, foreign_key="customers.id")
    year: int = Field(index=True, nullable=False)
    month: int = Field(index=True, nullable=False)
    month_amount: int = Field(nullable=False)
