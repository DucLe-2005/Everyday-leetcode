class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # time: O(n)
        # space: O(n)
        n = len(nums)
        left_products = [0 for _ in range(n)]
        curr = 1
        for i in range(n):
            curr *= nums[i]
            left_products[i] = curr
            
        right_products = [0 for _ in range(n)]
        curr = 1
        for i in range(n -1, -1, -1):
            curr *= nums[i]
            right_products[i] = curr
        
        res = []
        for i in range(n):
            prod = 1
            if i - 1 >= 0:
                prod *= left_products[i-1]
            if i + 1 < n:
                prod *= right_products[i+1]
            res.append(prod)
        
        return res




            
            