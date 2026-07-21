class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0,len(s) - 1
        while l < r:
            while s[l].isalnum() == False:
                l+= 1
            while s[r].isalnum() == False:
                r -= 1
            if s[l].lower() == s[r].lower():
                r -=1
                l +=1
            else:
                return False
        return True
            
             
