import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(n)]
check = [[0] * m for _ in range(n)]

board[0][0] = 1
queue = deque()
queue.append([0, 0])
while queue:
    tmp = queue.popleft()
    x = tmp[0]
    y = tmp[1]
    if x == n - 1 and y == m - 1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == "1":
            queue.append([nx,ny])
            board[nx][ny] = board[x][y] + 1

print(board[n - 1][m - 1])
