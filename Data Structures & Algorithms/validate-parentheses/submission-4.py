class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')' : '(', '}': '{', ']':'['}
        stack =[]
        for char in s:
            if char in closeToOpen:
                if stack[-1] == closeToOpen[char] and stack:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True