import sys

input = sys.stdin.readline
n = int(input())
friend = [list(input()) for _ in range(n)]
visit = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            if friend[j][k] == "Y" or (friend[j][i] == "Y" and friend[i][k] == "Y"):
                visit[j][k] = 1

res = 0
for cnt in visit:
    res = max(res, sum(cnt))
print(res)