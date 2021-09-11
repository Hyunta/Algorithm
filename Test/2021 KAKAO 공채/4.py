def calculate(info, ryan):
    score = 0
    for i in range(11):
        if info[i] or ryan[i]:
            if info[i] >= ryan[i]:
                score -= 10 - i
            else:
                score += 10 - i
    return score


def solution(n, info):
    result = []
    res = 0
    for i in range(10):
        tmp = n
        ryan = [0] * 11
        for j in range(i, 11):
            if info[j] < tmp:
                ryan[j] = info[j] + 1
                tmp -= info[j] + 1
        if tmp != 0:
            ryan[10] += tmp
        score = calculate(info, ryan)
        if res < score:
            res = score
            result = [ryan]
        # elif res == score:
        #     result.append(ryan)

    if res > 0:
        print(result)
    else:
        print([-1])


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
