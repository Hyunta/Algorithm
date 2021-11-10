import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
Max = 100001
time = [0] * Max

q = deque()
q.append(n)
while q:
    tmp = q.popleft()
    if tmp == k:
        print(time[tmp])
        break
    for move in [tmp - 1, tmp + 1, tmp * 2]:
        if 0 <= move < Max and not time[move]:
            time[move] = time[tmp] + 1
            q.append(move)
