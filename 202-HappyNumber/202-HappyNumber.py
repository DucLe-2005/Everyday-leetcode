class Solution:
    def isHappy(self, n: int) -> bool:
        def square(num):
            ans = 0
            while num > 0:
                remainder = num % 10
                ans += remainder**2
                num //= 10

            return ans
         
        
        slow, fast = n, square(n)

        while slow != fast:
            slow = square(slow)
            fast = square(square(fast))
        
        return slow == 1
