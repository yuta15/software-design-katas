from dataclasses import dataclass

from application import Format


@dataclass(frozen=True, slots=True)
class JsonFormat(Format[dict[str, str | int]]):
    pass


@dataclass(frozen=True, slots=True)
class CSVFormat(Format[list[list[str]]]):
    pass


@dataclass(frozen=True, slots=True)
class TSVFormat(Format[list[str]]):
    pass
