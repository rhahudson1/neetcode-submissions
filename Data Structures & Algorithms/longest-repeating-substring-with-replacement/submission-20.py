class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        charSet = set(s)
        
        for c in charSet:
            count = 0 # this will store how many non c's there are 
            l = 0
            for r in range(len(s)):
                if s[r] != c:
                    count += 1
                while (count) > k:
                    if s[l] != c:
                        count -= 1
                    l += 1
                maxLength = max((r-l+1),maxLength)
        return maxLength
