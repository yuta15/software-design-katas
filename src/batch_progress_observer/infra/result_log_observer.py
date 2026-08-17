import datetime
from pathlib import Path

from ..application.ports import NotifyData, NotifyObserver


class ResultLogObserver(NotifyObserver):
    def __init__(self):
        self._path = Path("../.log.txt")

    def notify(self, notify_data: NotifyData):
        with self._path.open(mode="a") as f:
            f.write(
                f"{datetime.datetime.now(datetime.UTC)} {notify_data.customer_id} {notify_data.customer_name} {notify_data.result.value} {notify_data.message}\n"
            )
