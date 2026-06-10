class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        nums = set(nums)
        for num in nums:
            if num > res and -num in nums:
                res = num
        
        return res