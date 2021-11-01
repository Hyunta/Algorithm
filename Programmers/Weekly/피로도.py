from itertools import permutations


def solution(k, dungeons):
    res = 0
    for con in permutations([i for i in range(len(dungeons))]):
        tmp_k, tmp_res = k, 0
        for i in con:
            req, val = dungeons[i]
            if tmp_k >= req:
                tmp_k -= val
                tmp_res += 1
        res = max(res, tmp_res)
    return res


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
