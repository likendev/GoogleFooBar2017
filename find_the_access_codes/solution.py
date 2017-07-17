def answer(l):
    # your code here
    inverse_l = l[::-1]

    result = []

    for item in l:
        triples = []
        l_queue = [a for a in inverse_l]
        triples.append(item)

        while l_queue:
            dividend = l_queue.pop()
            if dividend % item == 0:
                triples.append(dividend)
                if len(triples) == 2:
                    tmp_inverse_l = list(inverse_l)
                    for a in tmp_inverse_l:
                        if a % triples[-1] == 0 and a not in triples and triples[0] != triples[1]:
                            tmp_triples = list(triples)
                            tmp_triples.append(a)
                            if tmp_triples not in result:
                                result.append(tmp_triples)
                        elif triples[0] == triples[1]:
                            if l.count(a) == 3 and a == triples[1]:
                                tmp_triples = list(triples)
                                tmp_triples.append(a)
                                if tmp_triples not in result:
                                    result.append(tmp_triples)
                triples = [item]

    # print result
    return len(result)


print answer([1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8])
print answer([1, 1, 1, 2, 3, 4, 6])
