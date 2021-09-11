from collections import defaultdict


def solution(research, n, k):
    issue = {}
    seq = {}
    seq_val = defaultdict(list)
    tot = 2 * n * k
    for i in range(len(research)):
        daily = {}
        for x in research[i]:
            daily[x] = daily.get(x, 0) + 1
        daily = {key: v for key, v in daily.items() if v >= k}
        seq = {k: v for k, v in seq.items() if k in daily.keys()}
        for key, value in daily.items():
            seq[key] = seq.get(key, 0) + 1
            seq_val[key].append(value)
        for key in seq.keys():
            if seq[key] == n:
                seq[key] -= 1
                if sum(seq_val[key][-n:]) >= tot:
                    issue[key] = issue.get(key,0) + 1
    result = []
    for a,b in issue.items():
        if b == max(issue.values()):
            result.append(a)
    result.sort()
    if result:
        return result[0]
    else:
        return "None"


print(solution(["abaaaa", "aaa", "abaaaaaa", "fzfffffffa"], 2, 2))
print(solution(["yxxy", "xxyyy"], 2, 1))
print(solution(["yxxy", "xxyyy", "yz"], 2, 1))
print(solution(["xy", "xy"], 1, 1))
