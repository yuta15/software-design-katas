from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn

from ..application.ports import NotifyData, NotifyObserver


class TerminalProgressObserver(NotifyObserver):
    def __init__(
        self,
    ):
        self._progress = Progress(
            TextColumn("請求書 作成中..."),
            BarColumn(),
            TaskProgressColumn(),
        )
        self._task_id = None

    def notify(self, notify_data: NotifyData):
        if self._task_id is None:
            self._is_running = True
            self._task_id = self._progress.add_task("", total=notify_data.total_customers_number)
            self._progress.start()

        self._progress.update(task_id=self._task_id, advance=1)

        if self._progress.finished:
            self._progress.stop()
