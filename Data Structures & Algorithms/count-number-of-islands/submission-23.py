class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r,c):
            if (r < 0 or c < 0 or c == cols or r == rows or baord[r][c] != "1"):
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+ dr, c + dc)

            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    numIslands += 1
                    dfs(r,c)
