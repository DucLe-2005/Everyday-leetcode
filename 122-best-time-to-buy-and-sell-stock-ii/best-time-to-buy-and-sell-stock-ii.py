class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dfs with memoization
        # State: buying or selling
        n = len(prices)
        dp = {}
        def dfs(i, buying):
            if i == n:
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            skip = dfs(i + 1, buying)
            if buying:
                profit = max(skip, dfs(i + 1, False) - prices[i])
            else:
                profit = max(skip, dfs(i + 1, True) + prices[i])
            
            dp[(i, buying)] = profit
            return dp[(i, buying)]
        
        return dfs(0, buying=True)
