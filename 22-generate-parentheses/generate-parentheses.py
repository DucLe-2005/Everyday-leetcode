class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s: str = '', openN: int = 0, closeN: int = 0):
            if openN == closeN == n:
                res.append(s)
                return
            
            if openN < n:
                backtrack(s + "(", openN + 1, closeN)
            
            if closeN < openN:
                backtrack(s + ")", openN, closeN + 1)
            
        backtrack()
        return res