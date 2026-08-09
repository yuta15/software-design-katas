
from abc import ABC, abstractmethod

from domain import Data
from .models import Format, DataFormatType


class FormatterPort(ABC):
    def __init__(self, data:Data):
        self.data = data

    @abstractmethod
    def format(self) -> Format:...


class OutputterPort(ABC):
    def __init__(self, formatter:FormatterPort):
        self._formatter = formatter

    @abstractmethod
    def output(self) -> None: ...


class OutputSetFactory(ABC):
    @abstractmethod
    def create(self, format_type: DataFormatType, data:Data) -> OutputterPort:...
