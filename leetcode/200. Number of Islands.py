class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return

            if grid[x][y] != "1":
                return

            grid[x][y] = "X"
            for k in range(4):
                dfs(x + dx[k], y + dy[k])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        return cnt
