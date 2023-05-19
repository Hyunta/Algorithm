class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        possible_range = 0
        prev_possible_range = 0
        jump_count = 0

        for curr in range(len(nums)):
            if curr + nums[curr] > possible_range:
                possible_range = curr + nums[curr]

            if curr == prev_possible_range:
                jump_count += 1
                prev_possible_range = possible_range
                if prev_possible_range >= len(nums)-1:
                    return jump_count
        return -1
