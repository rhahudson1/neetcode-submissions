class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0], [-1,0], [0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0
        def addRoom(r,c):
            if ( r < 0 or r == rows or c < 0 or c == cols or (r,c) in visit or rooms[r][c] == -1 ):
                return
            visit.add((r,c))
            q.append([r,c])
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grids[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r,c + 1)
                addRoom(r,c - 1)
            dist += 1
        



        