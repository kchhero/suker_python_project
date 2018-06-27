def fn_expressive(upper=100000):
    total = 0
    for n in range(upper):
        total += n
    return total


def fn_terse(upper=100000):
    return sum(range(upper))


print(fn_expressive())
print(fn_terse())
