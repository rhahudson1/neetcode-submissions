class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
         l = 0
         num_rep = 0
         longest_sub = 0
         for r in range(len(s)- 1):
            if num_rep <= k:
                if s[l] == s[r]:
                    longest_sub += 1
                    r += 1
                else:
                    longest_sub += 1
                    num_rep += 1
            else:
                l += 1
         return longest_sub