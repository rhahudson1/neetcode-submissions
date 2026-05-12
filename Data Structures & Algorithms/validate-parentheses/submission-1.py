class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in closeToOpen:
                if stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False
