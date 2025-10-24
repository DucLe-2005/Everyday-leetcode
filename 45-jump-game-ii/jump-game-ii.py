class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        current_end = nums[0]
        farthest = 0
        jumps = 1
        for i in range(n-1): # stop at the last index
            farthest = max(farthest, i + nums[i])

            if i == current_end: # jump to the next farthest spot
                current_end = farthest
                jumps += 1
        
        return jumps