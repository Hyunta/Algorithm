class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        start_point = nums.index(target)
        last_point = -1
        for i in range(start_point, len(nums)):
            if nums[i] == target:
                last_point = i
            else:
                break
        return [start_point, last_point]