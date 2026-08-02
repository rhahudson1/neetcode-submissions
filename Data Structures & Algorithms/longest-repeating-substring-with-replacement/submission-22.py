class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        maxLength = 0
        for c in charSet:
            l = 0
            charSet = set()
            count = 0 # store the count of incorrect characters
            for r in range(len(s)):
                if s[r] != c:
                    count += 1
                    while count > k:
                        if s[l] != c:
                            count -=1 
                        l += 1
                maxLength = max(maxLength, (r -l + 1))
        return maxLength




        