class Solution:
    def calculate(self, s: str) -> int:
        # iterate s
        # If the sign is + or -,
        # get the sign and number and add that number to a stack
        # If the sign is * or /,
        # get the next number and last number from the stack to calculate, then push result to stack  
        # return the sum of all numbers from stack 

        stack = []
        operation = "+"
        num = 0

        def perform_operation(stack, num, operation):
            if operation == "+":
                stack.append(num)  
            elif operation == "-":
                stack.append(-num)  
            elif operation == "*":
                stack.append(stack.pop() * num)  
            else:
                stack.append(int(stack.pop() / num))

        for c in s:
            if c == " ":
                continue
            elif c.isdigit():
                num = num * 10 + int(c)
            else:
                perform_operation(stack, num, operation)
                operation = c
                num = 0
        
        perform_operation(stack, num, operation)
        return sum(stack)
                
            