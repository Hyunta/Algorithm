from itertools import combinations


def solution(number):
    res = 0
    c = list(combinations(number, 3))
    for x in c:
        if sum(x) == 0:
            res += 1
    return res
