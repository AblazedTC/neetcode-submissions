class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def search(r, c):
            nonlocal counter
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return

            #Update grid
            grid[r][c] = 0
            counter += 1

            #Search
            search(r + 1, c)
            search(r - 1, c)
            search(r, c + 1)
            search(r, c - 1)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    counter = 0
                    search(i, j)
                    ans = max(counter, ans)

        return ans

            
        