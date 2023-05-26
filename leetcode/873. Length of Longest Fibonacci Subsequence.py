class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        vals = set(arr)
        res = 0
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                first, second = arr[i], arr[j]
                curr = 2

                while first + second in vals:
                    first, second = second, first + second
                    curr += 1
                if curr > 2:
                    res = max(res, curr)
        return res