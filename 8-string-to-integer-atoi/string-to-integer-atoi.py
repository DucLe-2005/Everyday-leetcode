class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        res = 0
        n = len(s)
        sign = 1
        idx = 0

        if n == 0:
            return res
        
        if s[0] == "-":
            sign = -1
            idx = 1
        elif s[0] == "+":
            idx = 1
        elif not s[0].isdigit():
            return res

        while idx < n and s[idx].isdigit():
            res = res * 10 + ord(s[idx]) - ord('0')
            idx += 1
        
        res = res * sign

        MAX_CAP = 2**31 - 1
        MIN_CAP = -2**31

        if res > MAX_CAP:
            return MAX_CAP
        elif res < MIN_CAP:
            return MIN_CAP
        else:
            return res