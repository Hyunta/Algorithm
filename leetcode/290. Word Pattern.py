class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        word_map = {}
        for idx, val in enumerate(pattern):
            if val in word_map and word_map[val] != words[idx]:
                return False
            if val not in word_map.keys() and words[idx] in word_map.values():
                return False
            word_map[val] = words[idx]
        return True