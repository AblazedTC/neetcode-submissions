class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        rows, cols = len(grid), len(grid[0])

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and grid[nr][nc] != -1
                ):
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1