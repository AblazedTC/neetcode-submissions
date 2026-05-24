class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fruitLeft = 0
        minsPassed = 0
        q = deque()
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fruitLeft += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))

        while q and fruitLeft > 0:
            qLen = len(q)

            for _ in range(qLen):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and grid[nr][nc] == 1
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        fruitLeft -= 1

            minsPassed += 1

        return minsPassed if fruitLeft == 0 else -1