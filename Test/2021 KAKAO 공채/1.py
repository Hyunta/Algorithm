from collections import defaultdict


def solution(id_list, report, k):
    report = list(set(report))
    member = defaultdict(list)
    cnt = dict()
    for r in report:
        a, b = map(str, r.split())
        cnt[b] = cnt.get(b, 0) + 1
        member[a].append(b)
    result = []
    for id in id_list:
        tmp = member.get(id)
        tmp_cnt = 0
        if tmp:
            for x in tmp:
                if cnt[x] >= k:
                    tmp_cnt += 1
        result.append(tmp_cnt)
    return result



print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
