class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums) - 1):
            res.append(nums[i] | nums[i+1])
        
        return res