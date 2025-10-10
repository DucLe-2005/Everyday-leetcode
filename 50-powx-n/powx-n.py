class Solution:
    def myPow(self, x: float, n: int) -> float:
        # recurive binary exponentiation
        # if n == 0:
        #     return 1.0
        # if n < 0:
        #     return 1.0 / self.myPow(x , -1 * n)
        
        # if n % 2 == 0:
        #     return self.myPow(x * x, n // 2)
        # else:
        #     return x * self.myPow(x * x, (n - 1) // 2)

        # iterative binary exponentiation
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x 
            n *= -1

        res = 1
        while n > 0:
            if n % 2 != 0:
                res *= x
                n -= 1
            
            x *= x
            n //= 2
        
        return res
            


        
