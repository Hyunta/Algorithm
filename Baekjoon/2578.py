import sys
from collections import deque, defaultdict


def find_bingo():
    total = 0
    for r in range(5):
        if sum(visit[r]) == 5:
            total += 1

    tmp = list(k[::-1] for k in zip(*visit))
    for c in range(5):
        if sum(tmp[c]) == 5:
            total += 1

    rd, ld = 0, 0
    for i in range(5):
        if visit[i][i] == 1:
            rd += 1
        if visit[i][4 - i] == 1:
            ld += 1
    if ld == 5:
        total += 1
    if rd == 5:
        total += 1

    return total


input = sys.stdin.readline

board = defaultdict(list)
for i in range(5):
    tmp = list(map(int, input().split()))
    for j in range(5):
        board[tmp[j]].append(i)
        board[tmp[j]].append(j)

numbers = []
for _ in range(5):
    numbers += list(map(int, input().split()))
numbers = deque(numbers)

cnt = 0
visit = [[0] * 5 for _ in range(5)]
while numbers:
    num = numbers.popleft()
    cnt += 1
    i, j = board[num]
    visit[i][j] = 1
    if find_bingo() >= 3:
        print(cnt)
        break
