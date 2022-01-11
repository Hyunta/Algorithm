import sys

input = sys.stdin.readline

n = int(input())
current = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))


def changeZeroAndOne(num):
    return num * -1 + 1


def switch(switches, cnt):
    count = cnt
    if count == 1:
        switches[0] = changeZeroAndOne(switches[0])
        switches[1] = changeZeroAndOne(switches[1])
    for i in range(1, n):
        if switches[i - 1] != target[i - 1]:
            count += 1
            switches[i - 1] = changeZeroAndOne(switches[i - 1])
            switches[i] = changeZeroAndOne(switches[i])
            if i != n - 1:
                switches[i + 1] = changeZeroAndOne(switches[i + 1])
    if switches == target:
        return count
    else:
        return -1


res1 = switch(current[:], 0)
res2 = switch(current[:], 1)

if res1 == -1 or res2 == -1:
    print(max(res1, res2))
else:
    print(min(res1, res2))
