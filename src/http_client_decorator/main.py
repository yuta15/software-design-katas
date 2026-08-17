from .request import CacheRequest, ExecuteRequest, LogRequest, RetryRequest


def main():
    request = RetryRequest(CacheRequest(LogRequest(ExecuteRequest())))

    urls = [
        "aaa.com",
        "bbb.com",
        "ccc.com",
        "ddd.com",
        "eee.com",
        "fff.com",
        "ggg.com",
        "hhh.com",
        "iii.com",
        "jjj.com",
        "kkk.com",
        "lll.com",
        "mmm.com",
        "nnn.com",
        "ooo.com",
        "ppp.com",
        "qqq.com",
    ]
    for url in urls:
        text = request.get(url=url)
        print(text)


if __name__ == "__main__":
    main()
