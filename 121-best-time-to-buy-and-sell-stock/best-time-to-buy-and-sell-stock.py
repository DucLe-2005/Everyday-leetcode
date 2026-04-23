class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        res = 0

        for i in range(1, len(prices)):
            res = max(res, prices[i] - minimum_price)
            minimum_price = min(minimum_price, prices[i])
        
        return res