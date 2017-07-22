table = {1: 0, 2: 1}


def answer(n):
    # your code here
    n = int(n)

    return recursion(n)


def recursion(n):
    if n in table:
        return table[n]

    if n % 2 != 0:
        table[n] = min(recursion((n + 1) / 2) + 2,
                       recursion((n - 1) / 2) + 2)
    else:
        table[n] = recursion(n / 2) + 1

    return table[n]
