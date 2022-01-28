import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
total_rate = []
for _ in range(n):
    total_rate.append(list(map(int, input().split())))
max_value = 0
candidates = list(combinations([i for i in range(1, m + 1)], 3))
for candidate in candidates:
    sum = 0
    for rate in total_rate:
        sum += max(rate[candidate[0] - 1], rate[candidate[1] - 1], rate[candidate[2] - 1])
    max_value = max(sum, max_value)
print(max_value)
