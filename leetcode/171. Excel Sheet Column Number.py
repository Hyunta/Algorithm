class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0
        for idx,val in enumerate(columnTitle):
            curr_idx = n-idx -1
            curr_val = ord(val) - 64
            res += 26 ** curr_idx * curr_val
        return res

