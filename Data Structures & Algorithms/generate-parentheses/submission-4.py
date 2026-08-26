class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def dfS(openN, closedN): 
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                dfS(openN+1,closedN)
                stack.pop()
            if openN > closedN:
                stack.append(")")
                dfS(openN,closedN+1)
                stack.pop()
        dfS(0,0)
        return res