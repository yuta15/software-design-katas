from uuid import UUID, uuid4

from domain import IdGenerater


class UuidIdGenerater(IdGenerater):
    def generate(self) -> UUID:
        return uuid4()
