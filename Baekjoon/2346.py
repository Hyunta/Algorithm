import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
balloons = deque(enumerate(map(int, input().split())))
res = []

while balloons:
    idx, move = balloons.popleft()
    res.append(idx + 1)
    if move > 0:
        balloons.rotate(-move + 1)
    elif move < 0:
        balloons.rotate(-move)
print(*res)
