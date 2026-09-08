class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [[1,0], [-1,0], [0,1],[0,-1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
        
        level = -1
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if ( nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] != 1):
                        continue
                    q.append([nr,nc])
                    grid[nr][nc] = 2 
            level += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return level

        




        