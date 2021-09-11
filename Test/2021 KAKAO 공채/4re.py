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
    info_idx = []
    res = -10
    for idx, val in enumerate(info):
        info_idx.append([val, idx])

    info_idx.sort(key=lambda x: [x[0], -x[1]], reverse=True)
    for i in range(11):
        tmp = n
        ryan = [0] * 11
        for j in range(i, 11):
            tmp_val = info_idx[j]
            if tmp_val[0] < tmp:
                ryan[tmp_val[1]] = tmp_val[0] + 1
                tmp -= tmp_val[0] + 1
        if tmp != 0:
            ryan[10] += tmp
        score = calculate(info, ryan)
        if res < score:
            res = score
            result = [ryan]
        elif res == score:
            result.append(ryan)
    info_idx.sort(key=lambda x: [x[0], x[1]], reverse=True)
    for i in range(11):
        tmp = n
        ryan = [0] * 11
        for j in range(i, 11):
            tmp_val = info_idx[j]
            if tmp_val[0] < tmp:
                ryan[tmp_val[1]] = tmp_val[0] + 1
                tmp -= tmp_val[0] + 1
        if tmp != 0:
            ryan[10] += tmp
        score = calculate(info, ryan)
        if res < score:
            res = score
            result = [ryan]
        elif res == score:
            result.append(ryan)

    if res <= 0:
        return [-1]
    else:
        return result[0]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
print(solution(5, [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]))
