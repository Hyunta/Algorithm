class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        res = 0
        dp = [0] * 5001

        for c in coins:
            dp[c] += 1
            for i in range(c, amount+1):
                dp[i] += dp[i-c]
        return dp[amount]