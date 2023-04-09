def cpu_bound(number: int):
    total = 1
    arr = range(1, number + 1)
    for i in arr:
        for j in arr:
            for k in arr:
                total = i * j * k

    return total


if __name__ == "__main__":
    result = cpu_bound(100)
    print(result)
