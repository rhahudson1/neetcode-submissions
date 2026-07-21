class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        numIslands = 0
        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc + c
                    if (nr > rows or nr < 0 or nc < 0 or nc > cols or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"






        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    numIslands += 1
        return numIslands