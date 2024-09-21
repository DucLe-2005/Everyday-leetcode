class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = 0
        original = x

        if x < 0 or (x % 10 == 0 and x != 0): # Negative number or numbers end with 0 (excluding 0) is not palindrome
            return False
        
        while x > 0:
            digit = x % 10
            reversed = reversed * 10 + digit # Append digit at the end of reversed
            x //= 10

        return reversed == original
            
        
        