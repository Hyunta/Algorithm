import sys
from collections import defaultdict

input = sys.stdin.readline
n, d, k, c = map(int, input().split())
sushi = list(int(input()) for _ in range(n))
lt, rt = 0, 0
answer = 0
eaten_sushi = defaultdict(int)

eaten_sushi[c] += 1

while rt < k:
    eaten_sushi[sushi[rt]] += 1
    rt += 1

while lt < n:
    answer = max(answer, len(eaten_sushi))
    eaten_sushi[sushi[lt]] -= 1
    if eaten_sushi[sushi[lt]] == 0:
        del eaten_sushi[sushi[lt]]
    eaten_sushi[sushi[rt % n]] += 1
    lt += 1
    rt += 1
print(answer)
