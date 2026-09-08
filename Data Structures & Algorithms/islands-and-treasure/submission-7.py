class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visit = set()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        level = 0
        directions = [[1,0], [-1,0], [0,1],[0,-1]]
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nc == cols or nr == rows or grid[nr][nc] == -1 or (nr,nc) in visit:
                        continue
                    grid[nr][nc] = level
                    visit.add((nr,nc))
                    q.append([nr,nc])
            level += 1
        


