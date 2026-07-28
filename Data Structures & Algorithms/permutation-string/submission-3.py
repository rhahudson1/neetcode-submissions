class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False