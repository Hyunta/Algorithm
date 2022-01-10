import sys

input = sys.stdin.readline

n = int(input())

lt = 0
rt = 1
tot = 1
cnt = 0

while lt < n // 2 + 1:
    if tot < n:
        rt += 1
        tot += rt
    elif tot == n:
        cnt += 1
        rt += 1
        tot -= lt
        tot += rt
        lt += 1
    else:
        tot -= lt
        lt += 1

print(cnt + 1)
