import requests


def io_bound():
    # 요청을 보내기
    res = requests.get("https://google.com")

    return res


if __name__ == "__main__":
    for i in range(10):
        res = io_bound()
    print(res)
