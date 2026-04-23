class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, openN, closeN):
            if openN == closeN == n:
                res.append(s)
                return

            if openN < n:
                dfs(s + '(', openN + 1, closeN)
            
            if closeN < openN:
                dfs(s + ')', openN, closeN + 1)
        
        dfs("", 0, 0)
        return res

        # time O(n * 2^2n) (if there are n pairs, we have 2^2n possible strings, which is an upper bound. the real time complexity is lower. Each string includes a copy operation which takes O(n).
        # space: O(2n) = O(n)