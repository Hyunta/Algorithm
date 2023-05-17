class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sortedNums = sorted(set(nums))
        prev = sortedNums[0]

        max_len, curr_len = 1, 1

        for num in sortedNums[1:]:
            if num == prev + 1:
                curr_len += 1
            else:
                if max_len < curr_len:
                    max_len = curr_len
                curr_len = 1
            prev = num

        if max_len < curr_len:
            return curr_len
        return max_len
