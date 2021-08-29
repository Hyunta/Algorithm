from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 : house.append((i,j))
        elif board[i][j] == 2 : chicken.append((i,j))

res = sys.maxsize
for pick in combinations(chicken, m):
    tot = 0
    for h in house:
        tot += min([abs(h[0] - p[0]) + abs(h[1]-p[1]) for p in pick])
        if res <= tot: break
    if tot < res: res = tot
print(res)
