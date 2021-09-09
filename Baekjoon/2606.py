import sys

input = sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]
visited = [0 for _ in range(n)]
conn = int(input())
for _ in range(conn):
    a, b = map(int, input().rstrip().split())
    a -= 1
    b -= 1
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    visited[v] = 1
    for i in range(n):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(0)
print(sum(visited)-1)