import sys

input = sys.stdin.readline

n = int(input())
prices = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = prices[i]
    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[i - j] + prices[j])
print(dp[n])
