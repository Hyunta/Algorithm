import sys

input = sys.stdin.readline
n = int(input())
loc = list(map(str, input().rstrip()))
cnt = 0
for i in range(n-1):
    if loc[i] == 'E' and loc[i + 1] == 'W':
        cnt += 1
print(cnt)
