class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(gris[0])
        maxArea = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r,c):
            if ( r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            res = dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return 1 + res
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = dfs(r,c)
                    maxArea = max(res, maxArea)
        return maxArea


        