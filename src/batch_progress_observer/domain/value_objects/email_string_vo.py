import re
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EmailStringVo:
    value: str

    def __post_init__(self) -> None:
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if isinstance(self.value, str):
            if re.fullmatch(pattern, self.value):
                return
        raise ValueError(f"Invalid type CustomerNameVo. Please set specified pattern. Pattern: {pattern}")
