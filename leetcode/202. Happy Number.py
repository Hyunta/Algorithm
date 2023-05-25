class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        prev = n
        while True:
            curr = 0
            for x in str(prev):
                curr += int(x) ** 2
            if curr in visited:
                return False
            if curr == 1:
                break
            visited.add(curr)
            prev = curr
        return True
