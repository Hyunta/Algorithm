import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]


def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while queue:
        a, b, w = queue.popleft()
        if a == n - 1 and b == m - 1:
            return visited[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if board[x][y] == 1 and w == 1:
                    visited[x][y][0] = visited[a][b][1] + 1
                    queue.append([x, y, 0])
                elif board[x][y] == 0 and visited[x][y][w] == 0:
                    visited[x][y][w] = visited[a][b][w] + 1
                    queue.append([x, y, w])
    return -1


print(bfs())
