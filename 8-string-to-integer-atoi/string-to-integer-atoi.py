class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        res = 0
        neg = False

        if len(s) == 0:
            return res

        i = 0
        if s[0] == "-":
            neg = True
            i = 1
        elif s[0] == "+":
            i = 1
        
        while i < len(s) and s[i].isdigit():
            res = res * 10 + ord(s[i]) - ord('0')
            i += 1
        
        if neg:
            res = -res
        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        elif res > INT_MAX:
            return INT_MAX
        else:
            return res

