def fibonacci():
    i, j = 0, 1
    while True:
        yield j
        i, j = j, i + j


def fibonacci_transform():
    count = 0
    for f in fibonacci():
        if f > 5000:
            break

        print(f)
        if f % 2:
            count += 1

    return count


print(fibonacci_transform())
