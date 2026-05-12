class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxlength = 0
        for r in range(len(s)):
            length = 0
            if s[l] == s[r]:
                charSet.remove(s[l])
                length -= 1
            charSet.append(s[r])
            length += 1
            maxlength = max(length, r - l +1)
        return maxlength
