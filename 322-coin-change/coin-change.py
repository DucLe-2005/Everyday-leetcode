class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for x in range(amount + 1):
            for c in coins:
                if c <= x and dp[x - c] != -1:
                    if dp[x] == -1:
                        dp[x] = dp[x - c] + 1
                    else:
                        dp[x] = min(dp[x - c] + 1, dp[x])

        return dp[-1]
                

                