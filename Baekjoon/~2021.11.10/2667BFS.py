from collections import deque
import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(board, a, b):
    global n
    queue = deque()
    queue.append((a, b))
    board[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt.append(bfs(board, i, j))

cnt.sort()
print(len(cnt))
for x in cnt:
    print(x)
