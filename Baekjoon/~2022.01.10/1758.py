import sys

input = sys.stdin.readline

n = int(input())
tips = [int(input()) for _ in range(n)]
tips.sort(reverse=True)
tot = 0
for i in range(len(tips)):
    if tips[i] - i > 0:
        tot += tips[i] - i
print(tot)
