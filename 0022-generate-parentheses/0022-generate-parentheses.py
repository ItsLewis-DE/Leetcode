class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[]
        res =[]
        def backTracking(open,close):
            if open == close == n:
                res.append("".join(stack))
                return 
            if open < n:
                stack.append("(")
                backTracking(open+1,close)
                stack.pop()
            if close < open:
                stack.append(")")
                backTracking(open,close+1)
                stack.pop()
        backTracking(0,0)
        return res