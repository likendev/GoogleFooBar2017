import itertools

from collections import defaultdict


def answer(l):
    result = 0

    n = len(l)

    divides = defaultdict(list)

    for i, v in enumerate(l[:-1]):
        for j, nv in enumerate(itertools.islice(l, i + 1, n), i + 1):
            if isFactorOf(nv, v):
                divides[j].append((v, i))

    numDivisors = {k: len(v) for k, v in divides.iteritems()}

    for i in xrange(n - 1, -1, -1):
        if not i in divides:
            continue

        val = l[i]

        for (v, vi) in divides[i]:
            if vi in divides:
                result += numDivisors[vi]

    return result


def isFactorOf(n, m):
    if n == m:
        return True

    if n - m < m:
        return False

    return n % m == 0
