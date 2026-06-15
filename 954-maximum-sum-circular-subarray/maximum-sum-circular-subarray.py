class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(1)
        n = len(nums)
        curr_max = nums[0]
        best_max = nums[0]
        for i in range(1, n):
            curr_max = max(curr_max + nums[i], nums[i])
            best_max = max(curr_max, best_max)
        
        curr_min = nums[0]
        best_min = nums[0]
        for i in range(1, n):
            curr_min = min(curr_min + nums[i], nums[i])
            best_min = min(curr_min, best_min)
        
        if best_max < 0:
            return best_max

        return max(best_max, sum(nums) - best_min)

        
