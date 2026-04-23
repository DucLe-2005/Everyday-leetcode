class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        res = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res = max(res, prices[i] - minimum_price)
            else:
                minimum_price = min(minimum_price, prices[i])
        
        return res