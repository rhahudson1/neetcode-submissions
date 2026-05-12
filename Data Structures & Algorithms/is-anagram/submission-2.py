class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l ,r = 0, len(s) - 1
        while r > l:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True