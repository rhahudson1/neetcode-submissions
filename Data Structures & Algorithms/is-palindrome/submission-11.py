class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0,len(s) - 1
        while l <= r:
            if s[l].isalnum() == False:
                continue
            if s[r].isalnum() == False:
                continue 
