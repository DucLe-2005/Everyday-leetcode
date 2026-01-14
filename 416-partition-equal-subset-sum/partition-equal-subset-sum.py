class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp[i] = True if sum i can be formed from a subset in nums
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        subset_sum = total_sum // 2
        
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                # sum j can be formed if previously sum j can be formed
                # before we consider curr or previously sum j - curr can be formed
                dp[j] = dp[j] or dp[j - curr]
        
        return dp[-1]