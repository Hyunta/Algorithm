class Solution:
    def convert(self, st: str, numRows: int) -> str:
        if numRows == 1:
            return st
        idx, step = 0, 1
        words = [""] * numRows
        for s in st:
            words[idx] += s
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        return "".join(words)
