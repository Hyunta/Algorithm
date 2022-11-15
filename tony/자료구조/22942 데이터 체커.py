import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
squares = []
for i in range(n):
    x, r = map(int, input().split())
    squares.append([x - r, i, 0])
    squares.append([x + r, i, 1])
squares.sort(key=lambda x: x[0])


def check():
    stack = []
    for square in squares:
        x, num, state = square
        if state == 1:
            pop = stack.pop()
            if pop[1] != num:
                return "NO"
        else:
            stack.append(square)
    return "YES"


print(check())
