import sys

input = sys.stdin.readline
n, s = map(int, input().split())
seq = list(map(int, input().split()))
lt = 0
rt = 0
total = 0
answer = n + 1

while lt < n:
    if total >= s:
        total -= seq[lt]
        lt += 1
        answer = min(answer, rt - lt + 1)
    else:
        if rt >= n:
            break
        total += seq[rt]
        rt += 1

if answer > n:
    print(0)
else:
    print(answer)
