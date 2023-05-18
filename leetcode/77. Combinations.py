class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def find_combination(curr: list, pointer: int):
            if len(curr) == k:
                res.append(curr[:])
                return

            for i in range(pointer, n+1):
                curr.append(i)
                find_combination(curr, i+1)
                curr.pop()
        find_combination([], 1)
        return res
