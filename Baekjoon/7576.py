import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

m, n = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if farm[i][j] == 1:
            queue.append([i, j])

while queue:
    a, b = queue.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and farm[x][y] == 0:
            farm[x][y] = farm[a][b] + 1
            queue.append([x, y])

check = False
result = -2
for row in farm:
    for tom in row:
        if tom == 0:
            check = True
        result = max(result, tom)
if check:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result -1)
