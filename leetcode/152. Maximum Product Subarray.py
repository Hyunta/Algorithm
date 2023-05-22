class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        curr_max, curr_min, res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            comparing_targets = (curr, curr_max * curr, curr_min * curr)
            curr_max = max(comparing_targets)
            curr_min = min(comparing_targets)
            res = max(res, curr_max)
        return res