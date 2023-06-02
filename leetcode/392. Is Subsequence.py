class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr = 0
        for x in t:
            if curr == len(s):
                return True
            if x == s[curr]:
                curr += 1

        return True if curr == len(s) else False