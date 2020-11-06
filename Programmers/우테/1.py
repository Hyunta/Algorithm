def solution(arr):
    d = {}
    for n in arr:
        d[n] = d.get(n, 0) + 1
    answer = [0] * 3
    for k,v in d.items():
        if v < max(d.values()):
            answer[k-1] += max(d.values()) - v
    return answer



print(solution([2, 1, 3, 1, 2, 1]))
