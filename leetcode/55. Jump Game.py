class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_max_len = nums[0]
        for i in range(1, len(nums)):
            if curr_max_len == 0:
                return False
            curr_max_len -= 1
            curr_max_len = max(curr_max_len, nums[i])
        return True
