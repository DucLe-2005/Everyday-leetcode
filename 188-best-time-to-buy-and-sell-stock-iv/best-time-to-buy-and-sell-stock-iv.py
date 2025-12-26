class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if not prices or k == 0:
            return 0
        
        # More transactions can be done in n given days
        res = 0
        if k * 2 >= n:
            for buy, sell in zip(prices[:-1], prices[1:]):
                res += max(0, sell - buy)
            return res

        # dp[i][j][l] = balance
        # i: day, j: transactions used, l: 0=no stock, 1=hold stock
        dp =  [[[-float("inf")] * 2 for j in range(k + 1)] for i in range(n)]
        dp[0][1][1] = -prices[0]     # buy on the first day
        dp[0][0][0] = 0              # skip buying on the firt day
        for i in range(1, n):
            for j in range(k + 1):
                # No stock at the end of today
                # 1. Remain no stock, 2. Sell stock
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                # Can't hold stock without any transaction
                if j > 0:
                    # Has stock at the end of today
                    # 1. Hold stock from prev 2. Buy stock
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        
        res = max(dp[n - 1][j][0] for j in range(k + 1))
        return res
