class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 0
        prev = 0
        while i < len(nums) - 1 and nums[i] < nums[i+1]:
            i += 1
        
        if i == 0 or i == len(nums) - 1:
            return False
        
        prev = i
        while i < len(nums) - 1 and nums[i] > nums[i+1]:
            i += 1
        
        if i == len(nums) -1 or i == prev:
            return False
        
        prev = i    
        while i < len(nums) - 1 and nums[i] < nums[i+1]:
            i += 1
        
        return i == len(nums) - 1
    