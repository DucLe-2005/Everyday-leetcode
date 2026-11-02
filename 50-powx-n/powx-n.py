class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(m):
            if m == 0:
                return 1.0

            half = power(m // 2)

            if m % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            return 1.0 / power(-n)

        return power(n)