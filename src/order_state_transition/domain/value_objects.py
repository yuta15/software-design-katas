from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ItemNameVo:
    value:str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("Invalid type. Item Name set only strings")


@dataclass(frozen=True, slots=True)
class PriceVo:
    value:int

    def __post_init__(self) -> None:
        minimam_value = 0
        if not isinstance(self.value, int):
            raise TypeError("Invalid type. Price can only integer")
        
        if self.value < minimam_value:
            raise ValueError("Invalid value. Price can grater than 0")