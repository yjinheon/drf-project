"""
웸크롤링 : 웹페이지 구축
웸스크래핑 : 웹페이지에서 정보를 추출
"""
from bs4 import BeautifulSoup
import aiohttp  # 비동기 웹페이지 요청
import asyncio  # 비동기 처리

"""
aiohttp.ClientSession() : 비동기 웹페이지 요청을 위한 ClientSession 객체 생성
"""


async def fetch(session, url):
    async with session.get(url) as response:
        html = await response.text()  # await is used to wait for the response
        soup = BeautifulSoup(html, "html.parser")
        cont_thumb = soup.find_all("div", {"class": "cont_thumb"})
        for i in cont_thumb:
            title = i.find("p", {"class": "txt_thumb"})
            if title is not None:
                print(title.text)
        # print(cont_thumb)

        # print(html)


async def main():  # 코루틴 함수
    BASE_URL = "https://bjpublic.tistory.com/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C"
    urls = [f"{BASE_URL}?page={i}" for i in range(1, 10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.run(main())
