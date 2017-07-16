def answer(l):
    # your code here
    inverse_l = l[::-1]

    result = []
    new_result = []

    for item in l:
        triples = []
        l_queue = [a for a in inverse_l]
        triples.append(item)

        while l_queue:
            dividend = l_queue.pop()
            if dividend % item == 0:
                triples.append(dividend)
                if triples not in result and len(triples) == 2:
                    result.append(triples)
                    triples = [item]

    for item in inverse_l:
        triples = [a for a in result]
        l_queue = [a for a in l]
        while l_queue:
            dividend = l_queue.pop()
            if dividend % item == 0:
                for a in triples:
                    if dividend % a[-1] == 0 and len(a) < 3 and dividend not in a and a[0] != a[1]:
                        tmp_a = list(a)
                        tmp_var = list(a)
                        tmp_var.append(dividend)
                        if tmp_var not in triples:
                            triples.append(tmp_a)
                            a.append(dividend)
                            new_result.append(a)
                    elif dividend in a and a[0] == a[1] and len(a) < 3:
                        if l.count(dividend) == 3:
                            a.append(dividend)
                            new_result.append(a)
                result = triples

    # print new_result
    return len(new_result)


answer([1, 2, 3, 4, 5, 6])
answer([1, 1, 1])
