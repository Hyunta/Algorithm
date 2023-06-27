class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
            if map[num] == 3:
                del map[num]
        return list(map)[0]
