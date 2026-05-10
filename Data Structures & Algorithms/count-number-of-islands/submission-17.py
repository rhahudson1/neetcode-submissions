class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        path = set()
        num_Islands = 0
        def dfs(r,c):
            if (r < 0 or c < 0 or r == rows or c == cols or grid[r][c] != "1" or (r,c) in path ): 
                return
            path.add((r,c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in path and grid[r][c] == "1":
                    dfs(r,c)
                    num_Islands += 1
        return num_Islands
