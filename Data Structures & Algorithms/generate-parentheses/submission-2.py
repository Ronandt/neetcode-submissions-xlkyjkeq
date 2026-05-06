class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        def dfs(open = 0, close = 0 ):
            print(open, close)
            if open == n and close == n:
                res.append("".join(subset))
                return
            if (open < n):
                subset.append("(")
                dfs(open + 1,close)
                subset.pop()
                
            if (open > close):
                subset.append(")")
                dfs(open, close + 1)
                subset.pop()
        dfs()
        return res
