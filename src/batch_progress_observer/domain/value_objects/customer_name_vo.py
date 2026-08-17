import re
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CustomerNameVo:
    value: str

    def __post_init__(self) -> None:
        max_length = 128
        min_length = 0
        pattern = r"^[a-zA-Z0-9].*$"
        if isinstance(self.value, str):
            if min_length < len(self.value) < max_length:
                if re.fullmatch(pattern, self.value):
                    return
        raise TypeError(
            f"Invalid type CustomerNameVo. Please set length {min_length} ~ {max_length}. Allow string pattern is {pattern}"
        )
