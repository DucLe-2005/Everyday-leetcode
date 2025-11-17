class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        sign = 1 if x >0 else - 1
        res = 0
        x = -x if x < 0 else x

        while x:
            digit = x % 10
            res = res * 10 + digit
            if res > 2**31 - 1:
                return 0
            x //= 10
        
        return res * sign
