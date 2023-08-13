# global로 사용할 MongoDB 연결 객체를 생성
# router에서 사용할 수 있게끔 전역변수로 선언(init.py)
from motor.motor_asyncio import AsyncIOMotorClient  # 비동기 MongoDB
from odmantic import AIOEngine  # 비동기 ODM
from app.config import MONGO_DB_NAME, MONGO_URL


class MongoDB:
    """
    MongoDB와 연결을 위한 클래스
    MongoDB 연결을 위한 클라이언트와 엔진을 생성
    """

    def __init__(self):
        self.client = None
        self.engine = None

    def connect(self):
        self.client = AsyncIOMotorClient(MONGO_URL)
        # self.engine = AIOEngine(motor_client=self.client, database=MONGO_DB_NAME)
        self.engine = AIOEngine(client=self.client, database=MONGO_DB_NAME)
        print("DB와 성공적으로 연결이 되었습니다.")

    def close(self):
        self.client.close()  # disconnect from MongoDB


mongodb = MongoDB()  # Singleton Pattern : 단 한번만 instance를 생성해서 사용
