class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = row+ dr, col + dc
                    if (newRow in range(rows) and newCol in range(cols) and grid[newRow][newcol] == 1):
                        fresh -= 1
                        q.append((newRow,newCol))
                        grid[newRow][newCol] = 2
            time += 1
        if fresh == 0:
            return time
        return -1
                    