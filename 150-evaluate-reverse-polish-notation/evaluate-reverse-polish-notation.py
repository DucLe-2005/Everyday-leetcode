class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # time: O(n)
        # space: O(n)

        num_stack = []

        for t in tokens:
            if t == "+":
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif t == "-":
                a, b = num_stack.pop(), num_stack.pop()
                num_stack.append(b - a)
            elif t == "*":
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif t == "/":
                a, b = num_stack.pop(), num_stack.pop()
                num_stack.append(int(b / a))
            else:
                num_stack.append(int(t))

        return num_stack[0]