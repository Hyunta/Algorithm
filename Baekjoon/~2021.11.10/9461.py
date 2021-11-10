import sys

input = sys.stdin.readline
dp = [1, 1, 1] + [0] * 98
for i in range(3, 101):
    dp[i] = dp[i - 3] + dp[i - 2]

for _ in range(int(input())):
    tmp = int(input())
    print(dp[tmp - 1])
