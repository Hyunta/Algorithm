class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lt, rt = 0, len(nums) - 1
        while lt <= rt:
            mid = (lt + rt) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[rt]:
                if nums[mid] < target <= nums[rt]:
                    lt = mid + 1
                else:
                    rt = mid - 1
            else:
                if nums[lt] <= target < nums[mid]:
                    rt = mid - 1
                else:
                    lt = mid + 1
        return -1
