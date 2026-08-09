from abc import ABC, abstractmethod


class IdGenerater(ABC):
    @abstractmethod
    def generate(self):...