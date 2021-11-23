import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]

lt, rt = 0, k
answer = 0
ate_type = defaultdict(int)

for i in range(k):
    ate_type[belt[i]] += 1

ate_type[c] += 1
while lt < n:
    answer = max(answer, len(ate_type))
    ate_type[belt[lt]] -= 1
    if ate_type[belt[lt]] == 0:
        del ate_type[belt[lt]]
    ate_type[belt[rt % n]] += 1
    lt += 1
    rt += 1
print(answer)
