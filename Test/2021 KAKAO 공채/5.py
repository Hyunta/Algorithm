from collections import defaultdict


def solution(info, edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
    print(graph)
    res = 0

    def dfs(l, s, w):
        if s == w or not graph[l]:
            print(s)
            return
        else:
            for node in graph[l]:
                if info[node] == 0:
                    dfs(node, s + 1, w)
                else:
                    dfs(node, s, w + 1)

    dfs(0, 0, 0)


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
