class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()
        for r in range(rows):
            if heights[r][0]:
                pac.add((r,0))
            if heights[r][cols-1]:
                alt.add((r,cols-1))
        print(pac)

        