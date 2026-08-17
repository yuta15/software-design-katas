from uuid import UUID

from sqlmodel import Session, select

from ..application.ports import CustomerRepositoryPort
from ..domain.entities import Customer
from ..domain.value_objects import CustomerNameVo, EmailStringVo
from .db_schema import Customers


class CustomerRepository(CustomerRepositoryPort):
    def __init__(self, session: Session):
        self._session = session

    def get(self, customer_id: UUID) -> Customer:
        customer = self._get_customer_by_id(customer_id=customer_id)
        if customer:
            return Customer(
                id_=customer.id, name=CustomerNameVo(value=customer.name), email=EmailStringVo(value=customer.email)
            )
        raise ValueError("指定のIDは存在しないよ")

    def save(self, customer: Customer) -> None:
        exist_customer = self._get_customer_by_id(customer_id=customer.id_)
        if exist_customer:
            exist_customer.name = customer.name.value
            exist_customer.email = customer.email.value
        else:
            new_customer = Customers(id=customer.id_, name=customer.name.value, email=customer.email.value)
            self._session.add(new_customer)
        self._session.flush()

    def _get_customer_by_id(self, customer_id: UUID) -> Customers | None:
        return self._session.exec(select(Customers).where(Customers.id == customer_id)).first()
