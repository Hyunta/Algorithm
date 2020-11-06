def solution(rows, columns):
    graph = [[0] * columns for _ in range(rows)]
    x, y, i = 0, 0, 1
    cnt = 0
    while True:
        if graph[x][y] != 0:
            cnt += 1
        graph[x][y] = i
        i += 1
        if i % 2 == 0:
            y += 1
            y = y % columns
        else:
            x += 1
            x = x % rows
        if graph[x][y] != 0 and graph[x][y] % 2 == i % 2:
            break
        if i > (rows * columns) + cnt:
            break
    return graph


print(solution(3, 4))
print(solution(3, 3))
