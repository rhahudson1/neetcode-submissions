class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset = []
        res = []
        def dfs(openN, closedN):
            if n == openN == closedN:
                res.append(subset.join(""))
                return
            if openN < n:
                subset.append("(")
                dfs(openN+1, closedN)
                subset.pop()
            if openN > closedN:
                subset.append(")")
                dfs(openN, closedN+1)
                subset.pop()
        dfs(0,0)
        return res
        