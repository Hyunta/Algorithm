import sys

input = sys.stdin.readline

x, y, w, s = map(int, input().split())

cost1 = (x + y) * w
cost2 = 0
if (x + y) % 2 == 0:
    cost2 = max(x, y) * s
else:
    cost2 = (max(x, y) - 1) * s + w
cost3 = min(x, y) * s + (max(x, y) - min(x, y)) * w
result = min(cost1, cost2, cost3)
print(result)
