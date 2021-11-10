import sys

input = sys.stdin.readline

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    time = schedule[i][0]
    val = schedule[i][1]
    if time + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(val + dp[i + time], dp[i + 1])
print(dp[0])
