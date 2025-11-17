class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = 1 if x > 0 else - 1
        res = 0
        x = -x if x < 0 else x

        while x:
            digit = x % 10
            x //= 10
            if sign == 1 and res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0
            if sign == -1 and res > -INT_MIN // 10 or (res == -INT_MIN // 10 and digit > 8):
                return 0

            res = res * 10 + digit
        
        return res * sign
