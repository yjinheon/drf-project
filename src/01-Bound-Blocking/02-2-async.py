import time
import asyncio

# 서브루틴 : 하나의 진입점과 하나의 종료점을 가지는 함수를 의미
# 코루틴 : 다양한 진입점과 다양한 종료점을 가지는(루틴) 함수를 의미. 서브루틴의 일반화된 형태
# python 에서 코루틴은 async def 로 정의되며, await 키워드를 사용하여 다른 코루틴으로 제어권을 넘길 수 있다.


async def deliver(name, duration):
    """
    코루틴 함수를 활용한 동시성 프로그래밍
    """
    print(f"{name}에게 배달완료")
    await asyncio.sleep(duration)  # 다른 코루틴으로 제어권 넘김 // 비동기 함수를 처리할 때 사용
    print(f"{name} 식사 완료, {duration} 시간 소요")
    print(f"{name} 그릇 수거 완료")

    return duration


async def main():
    result: tuple
    result = await asyncio.gather(
        # gather 를 활용해 awaitable 객체들을 동시에 실행
        # awaitable 객체 일 경우 gather 안에 들어 있는 인자들을 동시성 기반으로 실행
        deliver("A", 1),
        deliver("B", 2),
        deliver("C", 3),
    )  #
    print(result)

async def main_sync():
    await deliver("A", 5)
    await deliver("B", 3)
    await deliver("C", 4)


async def main_task():
    """
    미리 예약을 해놓고 나중에 task를 실행
    """
    task1 = asyncio.create_task(deliver("A", 2))
    task2 = asyncio.create_task(deliver("B", 1))

    await task1
    await task2


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Processing time of {main.__name__}: {(end-start):.2f}")
