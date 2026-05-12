class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        l = 0
        charSet = Set()
        for r in range(len(s)):
            length = 0
            while s[l] == s[r]:
                charSet.remove(s[l])
                length -= 1
            charSet.append(s[r])
            length += 1
            maxlength = max(length, r-l +1)
        return maxlength