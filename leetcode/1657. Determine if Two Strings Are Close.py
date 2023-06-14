from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for x in word1:
            d1[x] += 1
        for x in word2:
            d2[x] += 1

        return sorted(d1.values()) == sorted(d2.values()) and sorted(d1.keys()) == sorted(d2.keys())
