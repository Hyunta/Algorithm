class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cnt = 0

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return False

            if grid[i][j] == 1:
                return True

            grid[i][j] = 1
            left = dfs(i - 1, j)
            right = dfs(i + 1, j)
            up = dfs(i, j + 1)
            down = dfs(i, j - 1)
            return left and right and up and down

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and dfs(i, j):
                    cnt += 1
        return cnt
