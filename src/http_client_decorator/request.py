import json
import pathlib
from abc import ABC, abstractmethod
from datetime import UTC, datetime


class Request(ABC):
    def __init__(self, requet: Request | None = None):
        self._request = requet

    @abstractmethod
    def get(self, url: str) -> str: ...


class RetryRequest(Request):
    def get(self, url: str) -> str:
        if self._request is None:
            raise AttributeError("なんもできない")

        max_retry = 3
        count = 0
        while count < max_retry:
            try:
                response = self._request.get(url=url)
                return response
            except Exception:  # noqa: BLE001
                print("リトライ")
                count += 1
                continue
        raise RuntimeError("リトライ上限")


class CacheRequest(Request):
    def get(self, url: str) -> str:
        if self._request is None:
            raise AttributeError("なんもできない")

        filename_path = pathlib.Path().cwd().joinpath("http_client_decorator/.request_cache.json")
        new_cache = {}
        if filename_path.exists():
            with filename_path.open(mode="r") as f:
                new_cache = json.load(f)

                for cached_url, cached_txt in new_cache.items():
                    if cached_url == url:
                        return cached_txt

        text = self._request.get(url=url)
        new_cache[url] = text

        with filename_path.open(mode="w") as f:
            json.dump(new_cache, f, indent=4)
        return text


class LogRequest(Request):
    def get(self, url: str) -> str:
        if self._request is None:
            raise AttributeError("なんもできない")

        logfile_path = pathlib.Path().cwd().joinpath("http_client_decorator/.logfile.txt")
        with logfile_path.open(mode="a") as f:
            try:
                f.write(f"{datetime.now(UTC)} 接続を開始します。URL: {url}\n")
                response = self._request.get(url=url)
                f.write(f"{datetime.now(UTC)} 接続を完了します。URL: {url}\n")
                return response
            except:
                f.write(f"{datetime.now(UTC)} 接続をに失敗しました。URL: {url}\n")
                raise


class ExecuteRequest(Request):
    def get(self, url: str) -> str:
        print("Request start")
        print("Request end")
        return f"url: {url}, text: dummy text"


class FailedRequest(Request):
    def get(self, url: str) -> str:
        raise RuntimeError("絶対に失敗する。")
