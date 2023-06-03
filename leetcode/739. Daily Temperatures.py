class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i,v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                t_idx, t_val = stack.pop()
                res[t_idx] = i - t_idx
            stack.append((i,v))
        return res