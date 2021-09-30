import sys


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    lt, rt = 0, distance
    while lt <= rt:
        mid = (lt + rt) // 2
        cur = 0
        remove_cnt = 0

        for rock in rocks:
            diff = rock - cur
            if diff < mid:
                remove_cnt += 1
            else:
                cur = rock

        if remove_cnt > n:
            rt = mid - 1
        else:
            answer = mid
            lt = mid + 1
    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
