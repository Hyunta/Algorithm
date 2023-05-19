class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        left = nums[0]
        for i in range(1,n):
            res[i] *= left
            left *= nums[i]

        right = nums[-1]
        for i in range(n-2,-1,-1):
            res[i] *= right
            right *= nums[i]
        return res
