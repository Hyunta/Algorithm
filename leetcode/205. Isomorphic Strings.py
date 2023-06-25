class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = dict()
        for i in range(len(s)):
            x = s[i]
            if (x in seen.keys() and seen[x] != t[i]) or (x not in seen.keys() and t[i] in seen.values()):
                return False
            seen[x] = t[i]
        return True