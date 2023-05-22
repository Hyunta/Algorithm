class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []

        def backtrack(curr: list, curr_visited: set):
            if len(curr) == len(nums):
                res.append(curr)
                return

            for i in nums:
                if i not in curr_visited:
                    backtrack(curr + [i], curr_visited + [i])

        backtrack([], [])
        return res