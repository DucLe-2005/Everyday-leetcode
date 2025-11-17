class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        

        sign = 1 if x >0 else - 1
        res = 0
        x = -x if x < 0 else x

        while x:
            digit = x % 10
            res = res * 10 + digit
            if not INT_MIN <= res <= INT_MAX:
                return 0

            x //= 10
        
        return res * sign
            