import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
result = []


def dfs(x, y):
    global cnt
    board[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][ny] == 1:
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            dfs(i,j)
            result.append(cnt)

print(len(result))
result.sort()
for x in result:
    print(x)


