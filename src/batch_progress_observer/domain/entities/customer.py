from uuid import UUID, uuid7

from ..value_objects import CustomerNameVo, EmailStringVo


class Customer:
    def __init__(self, id_: UUID, name: CustomerNameVo, email: EmailStringVo):
        self._id: UUID = id_
        self._name: CustomerNameVo = name
        self._email: EmailStringVo = email

    @property
    def id_(self) -> UUID:
        return self._id

    @property
    def name(self) -> CustomerNameVo:
        return self._name

    @property
    def email(self) -> EmailStringVo:
        return self._email

    @classmethod
    def new(cls, name: CustomerNameVo, email: EmailStringVo) -> Customer:
        return cls(id_=uuid7(), name=name, email=email)

    def __eq__(self, value: object):
        if isinstance(value, Customer) and self._id == value.id_:
            return True
        return False
