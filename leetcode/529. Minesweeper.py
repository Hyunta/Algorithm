class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def find_adjacent_mines(x, y):
            mines = 0
            for i in range(8):
                tx, ty = x + dx[i], y + dy[i]
                if 0 <= tx < m and 0 <= ty < n and board[tx][ty] == "M":
                    mines += 1
            return mines

        def dfs(x, y):
            mines = find_adjacent_mines(x, y)
            if mines:
                board[x][y] = str(mines)
                return board

            board[x][y] = "B"
            for i in range(8):
                tx, ty = x + dx[i], y + dy[i]
                if 0 <= tx < m and 0 <= ty < n and board[tx][ty] == "E":
                    dfs(tx, ty)
            return board

        m = len(board)
        n = len(board[0])

        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]

        cx = click[0]
        cy = click[1]

        if board[cx][cy] == "M":
            board[cx][cy] = "X"
            return board

        if board[cx][cy] == "E":
            return dfs(cx, cy)