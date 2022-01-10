import sys
from collections import defaultdict

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
seats = [[0] * n for _ in range(n)]
like_dict = defaultdict(list)
result = 0

for _ in range(n ** 2):
    info = list(map(int, input().split()))
    like_dict[info[0]] = info[1:]

    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1
    for i in range(n):
        for j in range(n):
            if seats[i][j] == 0:
                like_cnt = 0
                empty_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if seats[nx][ny] in info:
                            like_cnt += 1
                        if seats[nx][ny] == 0:
                            empty_cnt += 1
                if max_like < like_cnt or (max_like == like_cnt and max_empty < empty_cnt):
                    max_x = i
                    max_y = j
                    max_like = like_cnt
                    max_empty = empty_cnt
    seats[max_x][max_y] = info[0]

for i in range(n):
    for j in range(n):
        cnt = 0
        like = like_dict[seats[i][j]]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if seats[nx][ny] in like:
                    cnt += 1
        if cnt != 0:
            result += 10 ** (cnt - 1)

print(result)
