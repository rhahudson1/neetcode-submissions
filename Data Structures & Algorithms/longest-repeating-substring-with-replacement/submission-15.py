class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        longest_value = 0
        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r -l + 1) - count > k:
                   if s[l] == c:
                        count -= 1
                   l += 1
                longest_value = max(longest_value, r - l + 1)
        return longest_value


                
        