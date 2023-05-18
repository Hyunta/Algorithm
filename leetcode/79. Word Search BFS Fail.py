class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        m = len(board)
        n = len(board[0])

        def bfs(x:int, y:int) -> bool:
            if len(word) == 1:
                return True
            visited = list([False] * n for _ in range(m))
            queue = deque()

            visited[x][y] = True
            queue.append([x,y,1])

            while queue:
                cx, cy, curr_idx = queue.popleft()
                for k in range(4):
                    tx = cx + dx[k]
                    ty = cy + dy[k]
                    if 0 <= tx < m and 0 <= ty < n and not visited[tx][ty] and board[tx][ty] == word[curr_idx]:
                        visited[tx][ty] = True
                        if curr_idx == len(word) - 1:
                            return True
                        queue.append([tx,ty,curr_idx+1])
            return False

    

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if bfs(i,j):
                        return True
        return False