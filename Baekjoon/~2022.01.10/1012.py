import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        b, a = queue.popleft()
        for q in range(4):
            nb = b + dy[q]
            na = a + dx[q]
            if 0 <= nb < n and 0 <= na < m and field[nb][na] == 1 and visited[nb][na] == 0:
                visited[nb][na] = 1
                queue.append((nb, na))


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        i, j = map(int, input().split())
        field[j][i] = 1
    for y in range(n):
        for x in range(m):
            if field[y][x] == 1 and visited[y][x] == 0:
                bfs(y, x)
                cnt += 1
    print(cnt)
