from dataclasses import dataclass
from uuid import UUID


@dataclass
class Data:
    id: UUID


@dataclass
class User(Data):
    name: str
    age: int


@dataclass
class Dog(Data):
    name: str
    age: int
    kind: str


@dataclass
class Car(Data):
    kind: str
    maker: str
