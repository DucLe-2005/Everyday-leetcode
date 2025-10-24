class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # within the range of the jump range
        # choose the landing position that allows you to jump the farthest the next time you jump

        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])
        return True
        
            