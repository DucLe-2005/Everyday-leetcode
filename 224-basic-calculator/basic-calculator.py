class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0
        sign = 1
        stack = []  # numbers and operators

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                res += num * sign
                sign = 1 if c == "+" else -1
                num = 0                
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
                num = 0
            elif c == ")":
                res += num * sign
                num = 0
                s = stack.pop()
                n = stack.pop()
                res = n + res * s
        res += num * sign
        return res

        
        