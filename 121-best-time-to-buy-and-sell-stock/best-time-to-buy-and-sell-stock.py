class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = prices[0], prices[0]
        res = 0
        for price in prices:
            if price < low: # new low, reset sell-buy window
                low = price
                high = price
            if price > high:
                high = price
            
            res = max(res, high - low)
        
        return res