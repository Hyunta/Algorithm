class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        char_counts = defaultdict(int)
        for char in s:
            char_counts[char] += 1
        for i, char in enumerate(s):
            if char_counts[char] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)
        return len(s)