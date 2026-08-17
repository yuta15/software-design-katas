from .data import Car, Data, Dog, User
from .ports import IdGenerater


class NewEntityFactory:
    def __init__(self, id_generater: IdGenerater):
        self._id_generater = id_generater

    def create(self, **kwargs) -> Data:
        if kwargs is None:
            raise ValueError("Invalid value")

        if kwargs.get("name") is not None and kwargs.get("age") is not None and kwargs.get("kind"):
            return Dog(
                id=self._id_generater.generate(),
                name=kwargs["name"],
                age=kwargs["age"],
                kind=kwargs["kind"],
            )

        elif kwargs.get("name") is not None and kwargs.get("age") is not None:
            return User(id=self._id_generater.generate(), name=kwargs["name"], age=kwargs["age"])

        elif kwargs.get("kind") is not None and kwargs.get("maker") is not None:
            return Car(
                id=self._id_generater.generate(),
                kind=kwargs["kind"],
                maker=kwargs["maker"],
            )

        raise ValueError("Invalid value")
