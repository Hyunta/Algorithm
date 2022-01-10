import sys

input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack = []
res = []

for i in range(n):
    t = towers[i]
    while stack:
        if stack[-1][1] > t:
            res.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        res.append(0)
    stack.append([i, t])

print(*res)
