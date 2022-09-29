from collections import defaultdict


def solution(id_list, report, k):
    dic = defaultdict(set)
    for rep in report:
        a, b = rep.split(" ")
        dic[b].add(a)

    res = [0] * len(id_list)
    for value in dic.values():
        if len(value) >= k:
            for name in value:
                index = id_list.index(name)
                res[index] += 1

    return res


ids = ["muzi", "frodo", "apeach", "neo"]
reports = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
print(solution(ids, reports, 2))
