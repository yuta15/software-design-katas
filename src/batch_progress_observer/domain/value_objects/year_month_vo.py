from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class YearMonthVo:
    year: int
    month: int

    def __post_init__(self) -> None:
        min_year_value = 1
        min_month_value = 1
        max_month_value = 12

        if isinstance(self.year, int) and isinstance(self.month, int):
            if min_year_value < self.year and min_month_value <= self.month <= max_month_value:
                return
        raise ValueError(
            f"Invalid YearMonthVo. Please set Month {min_month_value} to {max_month_value}, year is grater than {min_year_value}"
        )
