class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        prev = prices[0]

        for i in range(1, n):
            curr = prices[i]
            if prev < curr:
                res += curr - prev
            prev = curr
        return res
