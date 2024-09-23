class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        l, r = 0, x

        while l <= r:
            mid_num = (l + r) // 2

            if mid_num * mid_num == x:
                return mid_num
            
            if mid_num * mid_num < x:
                l = mid_num + 1
            else:
                r = mid_num - 1
        
        return l - 1
            

        