class Solution:
    def calculate(self, s: str) -> int:
        cur_num = 0
        stack = []
        operation = '+'
        for i in range(len(s)):
            cur_char = s[i]
            if cur_char.isdigit():
                cur_num = cur_num * 10 + int(cur_char)
            
            # do the calculation when reached the next operation, white space, or the end of s
            if not cur_char.isdigit() and not cur_char.isspace() or i == len(s) - 1:
                if operation == "-":
                    stack.append(-cur_num)
                elif operation == "+":
                    stack.append(cur_num)
                elif operation == "*":
                    cur_num = stack.pop() * cur_num
                    stack.append(cur_num)
                elif operation == "/":
                    cur_num = int(stack.pop() / cur_num)  
                    stack.append(cur_num)
                operation = s[i]
                cur_num = 0

        res = 0
        for n in stack:
            res += n
        return res





