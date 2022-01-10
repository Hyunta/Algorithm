import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y, safe):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if reg[nx][ny] >= safe and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
reg = [list(map(int, input().split())) for _ in range(n)]
reg_min = min(map(min, reg))
reg_max = max(map(max, reg))
res = 1

for safe in range(reg_min, reg_max + 1):
    visited = [[0] * n for _ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(n):
            if reg[i][j] >= safe and visited[i][j] == 0:
                bfs(i, j, safe)
                tmp += 1
    res = max(tmp, res)
print(res)
