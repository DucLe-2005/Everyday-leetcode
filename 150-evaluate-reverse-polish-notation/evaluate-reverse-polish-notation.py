class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for t in tokens:
            if t == "+":
                operands.append(operands.pop() + operands.pop())
            elif t == "-":
                a = operands.pop() 
                b = operands.pop()
                operands.append(b - a)
            elif t == "*":
                operands.append(operands.pop() * operands.pop())
            elif t == "/":
                a = operands.pop() 
                b = operands.pop()
                operands.append(int(b / a))
            else:
                operands.append(int(t))
        return operands[0]