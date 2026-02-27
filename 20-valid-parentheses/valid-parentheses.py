class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if c in brackets:
                if not stack or brackets[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
    
        return True if not stack else False