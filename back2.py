import time


def deliver(name, duration):
    print(f"{name}에게 배달완료")
    time.sleep(duration)
    print(f"{name}식사 완료, {duration} 시간 소요")
    print(f"{name} 그릇 수거 완료")


# 시간측정
def check_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Processing time of {func.__name__}: {(end-start):.2f}")
        return result

    return wrapper


@check_time
def main():
    # 동기코드 - 순차적으로 실행
    deliver("A", 5)
    deliver("B", 3)
    deliver("C", 4)


if __name__ == "__main__":
    main()
