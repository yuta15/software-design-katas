import re
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExpenseNameVo:
    value: str

    def __post_init__(self) -> None:
        min_length = 0
        max_length = 128
        pattern = r"^[a-zA-Z0-9-_].*$"
        if isinstance(self.value, str):
            if min_length < len(self.value) < max_length:
                if re.fullmatch(pattern, self.value):
                    return
        raise ValueError(f"Invalid type ExpenseNameVo. Please set specified pattern. Pattern: {pattern}")
