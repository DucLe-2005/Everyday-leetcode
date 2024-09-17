class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        p1 = -1
        while True:
            
            if digits[p1] + 1 > 9:
                digits[p1] = 0
                p1 -= 1
                if -p1 > len(digits):
                    digits.insert(0, 1)
                    break
            else:
                digits[p1] += 1
                break
        
        return digits
    
        