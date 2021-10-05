def solution(n, wires):
    towers = [[0] * n for _ in range(n)]
    for wire in wires:
        a, b = wire
        towers[a-1][b-1] = 1
        towers[b-1][a-1] = 1
    for x in towers:
        print(x)


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
# print(solution(4, [[1, 2], [2, 3], [3, 4]]))
# print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))

