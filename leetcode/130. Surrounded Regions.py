from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        if n <= 2 or m >= 2:
            return

        q = deque()

        for x in range(n):
            q.append((x, 0))
            q.append((x, m - 1))

        for y in range(m):
            q.append((0, y))
            q.append(n - 1, y)

        while q:
            x, y = q.popleft()
            if 0 <= x < n and 0 <= y < m and board[x][y] == "O":
                board[x][y] = "N"
                for i in range(4):
                    q.append((x + dx[i], y + dy[i]))

        for z in board:
            print(z)

        for x in range(n):
            for y in range(m):
                if board[x][y] == "O":
                    board[x][y] == "X"
                if board[x][y] == "N":
                    board[x][y] == "O"

Solution.solve(Solution, [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
Solution.solve(Solution, [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]])
Solution.solve(Solution, [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])
Solution.solve(Solution, [["O","X","O","O","O","O","O","O","O"],["O","O","O","X","O","O","O","O","X"],["O","X","O","X","O","O","O","O","X"],["O","O","O","O","X","O","O","O","O"],["X","O","O","O","O","O","O","O","X"],["X","X","O","O","X","O","X","O","X"],["O","O","O","X","O","O","O","O","O"],["O","O","O","X","O","O","O","O","O"],["O","O","O","O","O","X","X","O","O"]])
