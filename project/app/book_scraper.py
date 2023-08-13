from app.config import get_secret
import aiohttp
import asyncio


class BookScraper:
    def __init__(self):
        self.API_URL = "https"
        self.API_ID = ""
        self.API_SECRET = ""

    @staticmethod  # static method is a method that is bound to a class rather than its object
    async def fetch_book_data(session, url, headers):
        """
        fetches book data from url
        """
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                res = await response.json()
                return res["items"]

    def unit_url(self, query, start):
        """
        returns a url for a single page
        """

        return {
            "url": f"{self.API_URL}?query={query}&display=15&start={start}",
            "headers": {
                "X-Naver-Client-Id": self.API_ID,
                "X-Naver-Client-Secret": self.API_SECRET,
            },
        }

    async def search(self, query, total_pages):
        """
        search for books
        """

        apis = [self.unit_url(query, 1 + i * 10) for i in range(total_pages)]

        async with aiohttp.ClientSession() as session:
            all_data = await asyncio.gather(
                *[
                    self.fetch_book_data(session, api["url"], api["headers"])
                    for api in apis
                ]  # * is used to unpack the list
            )
            #            print(all_data)
            result = []
            for data in all_data:  # 2중 리스트를 flatten
                if data is not None:
                    for book in data:
                        result.append(book)
            return result

    def get_book_data(self, query, total_pages):
        return asyncio.run(
            self.search(query, total_pages)
        )  # awaitable 객체가 아니라서 await을 쓸 수 없다.

    def hello(self):
        print("hello")


class NaverBookScraper(BookScraper):
    def __init__(self):
        self.API_URL = "https://openapi.naver.com/v1/search/book"
        self.API_ID = get_secret("NAVER_API_ID")
        self.API_SECRET = get_secret("NAVER_API_SECRET")


# if __name__ == "__main__":
#     nb = NaverBookScraper()

#     #    nb.get_book_data("파이썬", 1)
#     print(nb.get_book_data("파이썬", 1))
