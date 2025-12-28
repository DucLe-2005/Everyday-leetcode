class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        prev_op = "+"
        num = 0
        n = len(s)

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in "+-*/" or i == n - 1:
                if prev_op == "+":
                    stack.append(num)  
                elif prev_op == "-":
                    stack.append(-num)  
                elif prev_op == "*":
                    stack.append(stack.pop() * num)  
                else:
                    stack.append(int(stack.pop() / num))
                prev_op = c
                num = 0
 
        return sum(stack)
                
            