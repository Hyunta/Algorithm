class Solution:
    def maxArea(self, height: List[int]) -> int:
        lt, rt = 0, len(height) - 1
        res = 0
        while lt < rt:
            lv, rv = height[lt], height[rt]
            res = max(res, min(lv, rv) * (rt - lt))
            if lv <= rv:
                lt += 1
            else:
                rt -= 1
        return res
