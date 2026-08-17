from abc import ABC, abstractmethod
from uuid import UUID


class IdGenerater(ABC):
    @abstractmethod
    def generate(self) -> UUID: ...
