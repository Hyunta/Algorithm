class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = ""
        s = strs[0]
        l = strs[-1]
        for i in range(min(len(s), len(l))):
            if s[i] != l[i]:
                return res
            res += s[i]
        return res