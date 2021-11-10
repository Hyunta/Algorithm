import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]


def horizontal(x, val):
    if val in board[x]:
        return False
    return True


def vertical(y, val):
    for i in range(9):
        if val == board[i][y]:
            return False
    return True


def byThree(x, y, val):
    tmp_x = x // 3 * 3
    tmp_y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if val == board[tmp_x + i][tmp_y + j]:
                return False
    return True


def Dfs(cnt):
    if cnt == len(zeros):
        for row in board:
            for x in row:
                print(x, end=" ")
            print()
        sys.exit(0)
    else:
        for i in range(1, 10):
            tmp_x = zeros[cnt][0]
            tmp_y = zeros[cnt][1]

            if horizontal(tmp_x, i) and vertical(tmp_y, i) and byThree(tmp_x, tmp_y, i):
                board[tmp_x][tmp_y] = i
                Dfs(cnt + 1)
                board[tmp_x][tmp_y] = 0


Dfs(0)
