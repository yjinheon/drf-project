from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.models import mongodb
from app.models.book import BookModel
from app.book_scraper import NaverBookScraper

BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)


app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # book = BookModel(
    #     keyword="파이썬",
    #     publisher="BJPublic",
    #     price=1200,
    #     image="me.png",
    #     hhh="askljdlkas",
    # )
    # print(await mongodb.engine.save(book))  # DB에 저장
    # engine.save() 는 비동기 적으로 작동하는 코루틴이기 때문에 await를 붙여줘야 한다.
    return templates.TemplateResponse(
        "./index.html",
        {
            "request": request,
            "title": "책 검색 API",
        },  # index.html에 변수를 보낼 대 request 정보가 반드시 필요
    )


@app.get(
    "/search", response_class=HTMLResponse  # router라고 보면 된다.
)  # response_class=HTMLResponse => HTML로 응답
async def search(request: Request, q: str):
    print(q)
    # 우선적으로 설계를 해야지 개발속도가 느려지지 않는다.
    # 1. 검색어를 입력받는다.
    keyword = q
    naver_book_scraper = NaverBookScraper()

    books = await naver_book_scraper.search(keyword, 10)

    book_models = []

    for book in books:
        book_model = BookModel(
            keyword=keyword,
            publisher=book["publisher"],
            price=book["discount"],
            image=book["image"],
        )
        print(book_model)
        book_models.append(book_model)
        await mongodb.engine.save_all(
            book_models
        )  # 내부적으로 acyncio gather를 사용해 동시성 처리를 한다.

    # fastapi get decorator에서 q라는 인자를 받아서 q라는 변수에 저장
    # return templates.TemplateResponse(
    #     "./index.html",
    #     {
    #         "request": request,
    #         "title": "책 검색 API",
    #         "keyword": q,
    #     },  # index.html에 변수를 보낼 대 request 정보가 반드시 필요
    # )
    return templates.TemplateResponse(
        "./index.html",
        {
            "request": request,
            "title": "책 검색 API",
            "keyword": q,
            "books": books,  # 템플릿 엔진에 뿌려서 이미지데이터를 보여주기 위해 사용
        },
    )


@app.on_event("startup")  # 서버 구동시 시작되는 함수
def on_app_start():
    """before app starts"""
    print("Hello, Server!")
    mongodb.connect()  # 엔진과 클라이언트 자체는 app에 전역변수로 선언해서 app이 시작될 때 실행될 수 있도록 한다.


@app.on_event("shutdown")
def on_app_shutdown():
    print("Goodbye, Server!")
    """after app shutdown"""
    mongodb.close()
