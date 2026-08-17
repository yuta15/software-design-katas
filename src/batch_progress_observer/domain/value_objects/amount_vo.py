from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AmountVo:
    value: int

    def __post_init__(self) -> None:
        min_value = 0
        if isinstance(self.value, int):
            if min_value < self.value:
                return
        raise ValueError(f"Invalid AmountVo. Please set amount value {min_value} < 'value'")
