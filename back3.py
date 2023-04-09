# 4-1을 동시성 프로그래밍으로 변환
# import requests # 동기적 요청을 보낼 때 사용
import time
import os
import requests
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = [
        "https://apple.com",
        "https://www.google.com",
    ] * 50

    executer = ThreadPoolExecutor(max_workers=10)

    with requests.Session() as session:
        #        result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url) for url in urls]
        results = list(
            executer.map(fetcher, params)
        )  # map은 generator 객체이기 때문에 list로 변환


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed time: ", end - start)
