class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []

        for i, p in enumerate(pattern):
            stack.append(str(i + 1))
            if p == "I":
                while stack:
                    res.append(stack.pop())
        
        stack.append(str(len(pattern) + 1))    
        while stack:
            res.append(stack.pop())
    
        return "".join(res)