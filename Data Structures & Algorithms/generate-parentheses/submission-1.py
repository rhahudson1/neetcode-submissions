class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # can add ( only if you still have openings left (open < n)
        # can add ) only if it won't break validdity (close < open)
        # A string is complete and valid only when open == close == n
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

            
        backtrack(0,0)
        return res

                
