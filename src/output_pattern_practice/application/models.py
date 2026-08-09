from typing import Generic, TypeVar
from enum import Enum
from dataclasses import dataclass


FormatDataType = TypeVar("FormatData")


class DataFormatType(Enum):
    TSV="TSV"
    JSON="JSON"
    CSV="CSV"


@dataclass(frozen=True)
class Format(Generic[FormatDataType]):
    data:FormatDataType
