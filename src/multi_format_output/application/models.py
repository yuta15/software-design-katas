from dataclasses import dataclass
from enum import Enum


class DataFormatType(Enum):
    TSV = "TSV"
    JSON = "JSON"
    CSV = "CSV"


@dataclass(frozen=True)
class Format[T]:
    data: T
