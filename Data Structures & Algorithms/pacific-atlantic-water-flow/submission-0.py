class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()
        
        # We know that all bordering squares of the ocean are elgibile to have the ocean water in them
        # Row 1 belongs to pac set
        # Last Row belongs to atl set
        # Column 1 belongs to the pac set
        # Last column belongs to atl set
        # DFS search from each of the boxes in the set

        def dfs(r,c,visit,prevHeight):
            if (r < 0 or c < 0 or r == rows or c == cols or (r,c) in visit or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])            

        for r in range(rows):
            dfs(r,0, pac,heights[r][0])
            dfs(r,cols-1, atl,heights[r][cols-1])
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1,c, atl, heights[rows-1][c])
        res =[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res

        

        
