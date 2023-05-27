class Solution:
    def numSquares(self, n: int) -> int:
        sqrs = set()
        for i in range(1, n // 2 +1):
            if i ** 2 <= n:
                sqrs.add(i**2)
        dp = [i for i in range(n+1)]
        for sqr in sqrs:
            dp[sqr] = 1
            for i in range(sqr, n+1):
                dp[i] = min(dp[i], dp[i-sqr] + dp[sqr])
        return dp[n]