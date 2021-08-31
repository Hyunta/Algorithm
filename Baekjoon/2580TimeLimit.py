import sys
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]


def findCandidates(y, x):
    numbers = [i + 1 for i in range(9)]
    for k in range(9):
        if board[y][k] in numbers:
            numbers.remove(board[y][k])
        if board[k][x] in numbers:
            numbers.remove(board[k][x])
    y = y // 3
    x = x // 3
    for i in range(y * 3, (y + 1) * 3):
        for j in range(x * 3, (x + 1) * 3):
            if board[i][j] in numbers:
                numbers.remove(board[i][j])
    return numbers


def dfs(cnt):
    if cnt == len(zeros):
        for row in board:
            print(*row)
        return
    (i, j) = zeros[cnt]
    candidates = findCandidates(i, j)
    for num in candidates:
        board[i][j] = num
        dfs(cnt + 1)
        board[i][j] = 0
dfs(0)
