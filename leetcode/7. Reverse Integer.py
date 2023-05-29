class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            res = int("-" + "".join(str(x)[1:][::-1]))
        else:
            res = int("".join(str(x)[::-1]))
        return res if res.bit_length() < 32 else 0