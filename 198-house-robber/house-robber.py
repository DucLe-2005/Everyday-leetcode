class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        dp = [0] * (n + 3)
        for i in range(n - 1, -1, -1):
            dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])
        
        return max(dp[0], dp[1])

