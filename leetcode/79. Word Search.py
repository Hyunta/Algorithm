class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        m = len(board)
        n = len(board[0])

        def dfs(x: int, y: int, curr_idx: int) -> bool:
            if curr_idx == len(word):
                return True            

            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[curr_idx]:
                return False
            
            temp = board[x][y]
            board[x][y] = "#"
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if dfs(tx, ty, curr_idx+1):
                    return True
            board[x][y] = temp


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
