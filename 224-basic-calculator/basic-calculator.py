class Solution:
    def calculate(self, s: str) -> int:
        # Add operands to operands and operators to operators stack
        # when reach a closing parentheses ")", pop from operands and operators n times until reach an opening operands
        # calculate the current result and push to operands stack
        return self.evaluate(s, 0)[0]
        

    
    def evaluate(self, s, i):
        val = 0
        sign = 1

        while i < len(s) and s[i] != ")":
            num = 0
            if s[i] == " ":
                i += 1
                continue
            elif s[i] == "(":
                res, end = self.evaluate(s, i+1)
                val += res * sign
                i = end + 1
            elif s[i] in "+-":
                sign = 1 if s[i] == "+" else -1
                i += 1
            else:
                while i < len(s) and s[i] in "0123456789":
                    num = num * 10 + int(s[i])
                    i += 1
                val += num * sign
        
        return (val, i)








        
        