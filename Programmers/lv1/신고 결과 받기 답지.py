def solution(id_list, report, k):
    res = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            res[id_list.index(r.split()[0])] += 1
    return res


ids = ["muzi", "frodo", "apeach", "neo"]
reports = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
print(solution(ids, reports, 2))
