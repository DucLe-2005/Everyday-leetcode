class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = ""
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = "0" if i >= len(a) else a[i]
            digitB = "0" if i >= len(b) else b[i]
            
            total = int(digitA) + int(digitB)+ (carry % 2) 
            result = str(total % 2) + result
            carry = total // 2
        
        if carry:
            result = "1" + result

        return result        

        