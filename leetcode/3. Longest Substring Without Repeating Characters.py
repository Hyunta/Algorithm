class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt = 0
        seen = {}
        res = 0
        for rt in range(len(s)):
            print(lt, rt, res)
            if s[rt] not in seen:
                res = max(res, rt - lt + 1)
            else:
                if seen[s[rt]] < lt:
                    res = max(res, rt - lt + 1)
                else:
                    lt = seen[s[rt]] + 1
            seen[s[rt]] = rt
        return res
