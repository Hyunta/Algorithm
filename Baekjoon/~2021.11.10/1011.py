import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    dis = y - x
    cnt = 0
    move = 1
    tot = 0
    while tot < dis:
        cnt += 1
        tot += move
        if cnt % 2 == 0:
            move += 1
    print(cnt)
