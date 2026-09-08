class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cache = []
        for i in range(n):
            row = []
            for c in range(n):
                row.append(False)
            cache.append(row)
        res = 0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] or (j-i <= 2 or cache[i+1][j-1]):
                    cache[i][j] = True
                    res += 1
        return res