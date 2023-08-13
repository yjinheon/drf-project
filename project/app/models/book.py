from odmantic import Model

# odmantic is a library for using MongoDB with pydantic data models.
# ORM의 NO SQL 버전이 odm 이다 . odmantic은 pydantic을 사용한다.

# 하나의 Document에 대응한다.
# DB -> collection -> Document


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = "books"
