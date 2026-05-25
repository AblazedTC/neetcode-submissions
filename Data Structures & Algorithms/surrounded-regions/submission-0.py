class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            board[i][j] = "T"

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        board[nr][nc] == "O"
                    ):
                        q.append((nr, nc))
                        board[nr][nc] = "T"

        for i in range(rows):
            for j in range(cols):
                if (i in (0, rows - 1) or j in (0, cols - 1)) and board[i][j] == "O":
                    bfs(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"