class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr, cnt = nums[0], 1
        for x in nums[1:]:
            cnt += 1 if curr == x else -1
            if not cnt:
                curr = x
                cnt = 1
        return curr