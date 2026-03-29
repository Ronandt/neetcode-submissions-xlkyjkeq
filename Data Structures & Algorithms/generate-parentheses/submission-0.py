class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def dfs(open = 0, close = 0 ):
            if open == close == n:
                res.append("".join(subset))
                return
            if open < n:
                subset.append("(")
                dfs(open = open + 1, close = close)
                subset.pop()
            if open > close:
                subset.append(")")
                dfs(open = open, close = close + 1)
                subset.pop()
        dfs()
        return res

            
