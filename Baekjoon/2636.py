import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def find_air():
    visited = [[False] * col for _ in range(row)]

    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    cnt = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                elif board[nx][ny] == 1:
                    board[nx][ny] = 0
                    cnt += 1
                    visited[nx][ny] = True
    cheese.append(cnt)
    return cnt


row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
cheese = []

time = 0

while True:
    time += 1
    cnt = find_air()
    if cnt == 0:
        break
print(time - 1)
print(cheese[-2])
