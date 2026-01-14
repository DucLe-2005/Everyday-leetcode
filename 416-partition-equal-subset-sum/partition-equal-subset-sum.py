class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # There are two decisions we can make to a number: include or not include
        # dp[i][j] = True if sum j can be formed by array elements in subset nums[0] -> nums[i]
        # if dp[i-1][j] = True, then dp[i][j] = True -> not include nums[i]
        # if dp[i-1][j - nums[i]] = true, then dp[i][j] = true -> include nums[i]

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        dp = [[False] * (subset_sum+1) for _ in range(len(nums) + 1)]
        
        dp[0][0] = True

        for i in range(1, len(nums) + 1):
            curr = nums[i - 1] 
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i-1][j]
                else: 
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - curr]
        
        return dp[-1][-1]