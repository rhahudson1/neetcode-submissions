class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        maxLength = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in charMap and charMap[char] >= left:
                left = charMap[char] + 1
            charMap[char] = right
            currentLength = right - left + 1
            maxLength = max(maxLength, currentLength)
        return maxLength