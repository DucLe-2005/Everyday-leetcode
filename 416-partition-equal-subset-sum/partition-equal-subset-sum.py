class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @lru_cache(maxsize=None)
        def dfs(nums, n, subset_sum):
            if subset_sum == 0:
                return True
            
            if n == 0 or subset_sum < 0:
                return False
            
            return dfs(nums, n - 1, subset_sum - nums[n - 1]) or dfs(nums, n - 1, subset_sum)

        
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n, subset_sum)




