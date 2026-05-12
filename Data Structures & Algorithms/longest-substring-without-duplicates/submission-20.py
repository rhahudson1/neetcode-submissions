class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,1
        max_length = 0
        while r < len(s):
            length = 0
            if s[l] == s[r]:
                l += 1
            else:
                length += 1
            r += 1
            max_length = max(max_length, length)
        return max_length
