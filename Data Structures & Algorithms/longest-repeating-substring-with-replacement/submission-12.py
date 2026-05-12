class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        num_replace = 0
        for r in range(len(s)):
            if num_replace <= k:
                if s[l] == s[r]:
                    res = max(res, r -l +1)
                else:
                    res = max(res, r -l +1)
                    num_replace += 1
            else:
                l += 1
        return res
