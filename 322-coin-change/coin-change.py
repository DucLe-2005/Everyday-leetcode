class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Reasoning: 
        # Since amount 7 = amount 5 + coin 2,
        # the least # of coins for 7 = the least # of coins to make up 5 plus 1
        # dp[i] = dp[i - coin] + 1
        # time: O(n * m), space: O(n), n = amount, m( = # of coins

        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0 and dp[i - c] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - c] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[-1]