class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1count = [0] * 26
        t1count = [0] * 26
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            s1count[index] += 1
        for i in range(len(t)):
            index = ord(t[i]) - ord('a')
            t1count[index] += 1
        matches = 0
        for i in range(len(s2count)):
            if s1count[i] == t1count[i]:
                matches += 1
        return matches == 26
