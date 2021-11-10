import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

check = [0] * (n + 1)

queue = deque()
queue.append(a)

while queue:
    tmp = queue.popleft()
    for n in graph[tmp]:
        if check[n] == 0:
            check[n] = check[tmp] + 1
            queue.append(n)
print(check[b] if check[b] > 0 else -1)
