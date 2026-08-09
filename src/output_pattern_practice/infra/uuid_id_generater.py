from uuid import uuid4, UUID

from domain import IdGenerater


class UuidIdGenerater(IdGenerater):
    def generate(self) -> UUID:
        return uuid4()