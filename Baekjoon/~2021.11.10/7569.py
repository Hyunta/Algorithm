import sys
from collections import deque

input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
farm = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if farm[z][y][x] == 1:
                queue.append([x, y, z])

while queue:
    a, b, c = queue.popleft()
    for i in range(6):
        x = a + dx[i]
        y = b + dy[i]
        z = c + dz[i]
        if 0 <= x < m and 0 <= y < n and 0 <= z < h and farm[z][y][x] == 0:
            queue.append([x, y, z])
            farm[z][y][x] = farm[c][b][a] + 1

tot = 0
for x in farm:
    for row in x:
        for item in row:
            if item == 0:
                print(-1)
                exit(0)
        tot = max(tot, item)
print(tot - 1)


