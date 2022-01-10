import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]

sqr = min(n, m)
res = 0

for i in range(n):
    for j in range(m):
        for k in range(res, sqr):
            if i + k < n and j + k < m:
                if graph[i][j] == graph[i][j+k] == graph[i+k][j] == graph[i+k][j+k]:
                    res = k
print((res+1)**2)


