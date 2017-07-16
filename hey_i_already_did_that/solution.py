def answer(n, b):
    # your code here
    k = len(n)

    newNum = n

    result = []

    a = 0

    while True:
        x_str = ''.join(str(a) for a in sortDescNum(newNum))
        y_str = ''.join(str(a) for a in sortAscNum(newNum))

        x_int = int(x_str,b) # convert to integers in base 10
        y_int = int(y_str,b)
        z_int = abs(x_int - y_int)
        z_str_list = numToBase(z_int, b) # convert back to base b, still in integer form
        z_str = (''.join(str(z) for z in z_str_list)).zfill(k)

        if z_str not in result:
            result.append(z_str)
            newNum = z_str
        else:
            a = result.index(z_str)
            a = len(result) - a
            break

    return a


    # if n == 0:
    #     return 0
    # d = []
    # while n:
    #     d.append(int(n % b))
    #     n /= b
    # return ''.join(map(str,d[::-1]))


def sortDescNum(n):
    return sorted(list(n),key=int,reverse=True)


def sortAscNum(n):
    return sorted(list(n))


def numToBase(n, b):
    if n == 0:
        return [0]
    digits = []

    if b != 10:
        while n:
            digits.append(int(n % b))
            n /= b
        return digits[::-1]
    else:
        return str(n)

# answer("210022",3)
# answer("002220",3)
# answer("012210",3)
print answer("210022",3)
