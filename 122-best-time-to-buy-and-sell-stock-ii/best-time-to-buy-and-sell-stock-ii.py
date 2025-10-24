class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: buy and sell
        # If buy, buy or skip
        # If sell, sell or skip
        dp = {}  # (i, buying): profit
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            skip = dfs(i+1, buying)
            if buying:
                amount = max(skip, dfs(i+1, not buying) - prices[i])
            else:
                amount = max(skip, prices[i] + dfs(i+1, not buying))
            
            dp[(i, buying)] = amount
            return dp[(i, buying)]
        
        return dfs(0, True)
