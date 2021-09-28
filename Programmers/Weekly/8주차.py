def solution(sizes):
    first = []
    second = []
    for a,b in sizes:
        first.append(max(a,b))
        second.append(min(a,b))
    return max(first) * max(second)