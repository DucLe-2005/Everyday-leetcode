class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        base = 1
        sum = 0
        while n:
            if n % 10 != 0:
                d = n % 10
                x += d * base
                base *= 10
                sum += d
            n //= 10
        
        return x * sum
            