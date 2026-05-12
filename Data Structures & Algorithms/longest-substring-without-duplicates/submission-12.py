class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            len = max(len, r - l + 1)
        return len