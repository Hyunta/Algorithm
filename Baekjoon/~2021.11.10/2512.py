import sys

input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
budget = int(input())

lt = 0
rt = max(requests)

while lt <= rt:
    mid = (lt+rt)//2
    tot = 0
    for request in requests:
        if request >= mid:
            tot += mid
        else:
            tot += request

    if tot > budget:
        rt = mid - 1
    else:
        lt = mid + 1

print(rt)