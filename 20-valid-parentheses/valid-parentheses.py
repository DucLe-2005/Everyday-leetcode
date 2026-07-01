class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for c in s:
            if c in close_to_open:
                if not stack or close_to_open[c] != stack[-1]:
                    return False
                stack.pop()  
            else:
                stack.append(c)  
        
        return len(stack) == 0