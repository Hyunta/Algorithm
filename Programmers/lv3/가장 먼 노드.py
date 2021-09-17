from collections import deque


def solution(n, edge):
    graph = {}
    visited = [0] * n
    for x in edge:
        graph[x[0]] = graph.get(x[0], []) + [x[1]]
        graph[x[1]] = graph.get(x[1], []) + [x[0]]
    queue = deque()
    queue.append(1)
    visited[0] = 1
    while queue:
        nodes = len(queue)
        for i in range(nodes):
            current = queue.popleft()
            for c in graph[current]:
                if visited[c-1] == 0:
                    visited[c-1] = 1
                    queue.append(c)
    return nodes




print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
