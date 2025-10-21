class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # get the number value of num1
        # from right to left, multiple each digit in num2 to num1 and add to ans variable
        # let ans *= 10 after each iteration

        number1 = 0
        for num in num1:
            number1 = number1 * 10 + ord(num) - ord('0')
        
        res = number1 * (ord(num2[0]) - ord('0'))
        for num in num2[1:]:
            res = res * 10 + number1 * (ord(num) - ord('0'))
        
        return str(res)