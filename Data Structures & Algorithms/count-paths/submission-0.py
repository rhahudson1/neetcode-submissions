class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cache[r][c] = for each position, # of ways we can reach the destination
        # res = R + D
        # cache[r][c] = cache[r][c+1] (one to the right) + cache[r+1][c] (one below)
        # m = rows
        # n = cols
        row = [1] * n # this is the bottom row. Every cell has exactly one path
        for i in range(m-1): 
            newRow =[1] * n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]



         
        