from abc import ABC, abstractmethod

from .models import NotifyData


class NotifyObserver(ABC):
    @abstractmethod
    def notify(self, notify_data: NotifyData) -> None: ...


class Notifier(ABC):
    def __init__(self, observers: list[NotifyObserver]):
        self._observers = observers

    def subscribe(self, observer: NotifyObserver) -> None:
        if isinstance(observer, NotifyObserver):
            self._observers.append(observer)
            return
        raise TypeError("Invalid observer")

    @abstractmethod
    def notify(self, notify_data: NotifyData) -> None: ...
