class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1. Greedy: continuously update the farthest jumpable index
        # time complexity: O(n), space complexity: O(1)
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])

        return True