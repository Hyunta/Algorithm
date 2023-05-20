class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_pelindrome(s: str):
            return s == s[::-1]

        def dfs(idx: int, curr: list):
            if idx == len(s):
                res.append(curr)
                return

            for j in range(idx, len(s)):
                substring = s[idx:j + 1]
                if is_pelindrome(substring):
                    dfs(j + 1, curr + [substring])
            return

        dfs(0, [])
        return res
