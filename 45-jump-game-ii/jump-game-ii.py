class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        farthest = nums[0]
        current_end = nums[0]
        jumps = 1

        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            
            if i == current_end:
                current_end = farthest
                jumps += 1
        
        return jumps
