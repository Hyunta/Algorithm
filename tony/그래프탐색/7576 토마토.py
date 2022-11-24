import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

while queue:
    a, b = queue.popleft()

    for i in range(4):
        tx, ty = a + dx[i], b + dy[i]
        if 0 <= tx < n and 0 <= ty < m and box[tx][ty] == 0:
            box[tx][ty] = box[a][b] + 1
            queue.append([tx, ty])

is_not_finished = False
max_day = -2
for row in box:
    for item in row:
        if item == 0:
            is_not_finished = True
        max_day = max(item, max_day)

if is_not_finished:
    print(-1)
else:
    print(max_day - 1)
