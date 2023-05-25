class Solution:
   def moveZeroes(self, nums):
       lt = 0
       for rt in range(len(nums)):
           if (nums[rt] != 0):
               nums[lt], nums[rt] = nums[rt], nums[lt]
               lt += 1