import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline
n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            space[i][j] = 2
            start = [i, j]

exp = 0
cnt = 0


def bfs(i, j):
    visit = [[0] * n for _ in range(n)]
    visit[i][j] = 1
    eat = []
    dist = [[0] * n for _ in range(n)]
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if space[nx][ny] <= space[i][j] or space[nx][ny] == 0:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                if 0 < space[nx][ny] < space[i][j]:
                    eat.append([nx, ny, dist[nx][ny]])
    if not eat:
        return [-1, -1, -1]
    eat.sort(key=lambda x: (x[2], x[0], x[1]))
    return eat[0]


while True:
    i, j = start
    ex, ey, dist = bfs(i, j)
    if ex == -1: break
    space[ex][ey] = space[i][j]
    space[i][j] = 0
    start = [ex,ey]
    exp += 1
    if exp == space[ex][ey]:
        exp = 0
        space[ex][ey] += 1
    cnt += dist
print(cnt)
