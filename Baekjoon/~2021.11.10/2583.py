import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = -1

res = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt = 1
            queue = deque()
            queue.append([i, j])
            graph[i][j] = cnt

            while queue:
                y, x = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
                        graph[ny][nx] = 1
                        queue.append([ny, nx])
                        cnt += 1
            res.append(cnt)
res.sort()
print(len(res))
print(*res)
