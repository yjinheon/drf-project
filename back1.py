# 세션 : 서버와 클라이언트 사이의 연결을 유지시켜 주는 상태
# 기본적으로 session을  열었으면 반드시 닫아줘야 한다.
# 따라서 with 구문을 사용한다.

import requests
import time


def fetcher(session, url):
    """session을 사용하여 url에 접속하여 html을 가져온다."""
    with session.get(url) as response:
        return response.text


def main():
    urls = [
        "https://www.naver.com",
        "https://instagram.com",
        "https://www.google.com",
    ] * 10

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed time: ", end - start)
