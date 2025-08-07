class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        cur = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(cur))
                return
            
            for c in digitMap[digits[i]]:
                cur.append(c)
                dfs(i + 1)
                cur.pop()

        dfs(0)
        return res

    # n = len(digits)
    # time complexity: O(4^n)
    # space complexiy: O(n) stack, O(4^n)