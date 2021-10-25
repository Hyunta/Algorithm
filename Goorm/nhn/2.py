n, k = map(int, input().split())
board = dict()
for _ in range(n):
    tmp = list(map(int, input().split()))
    for x in tmp:
        board[x] = board.get(x, 0) + 1



