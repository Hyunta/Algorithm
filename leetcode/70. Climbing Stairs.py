class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [1, 2, 3] + [0] * (n - 2)
        if n < 3:
            return ans[n - 1]
        for i in range(3, n):
            ans[i] = ans[i - 2] + ans[i - 1]
        return ans[n - 1]
