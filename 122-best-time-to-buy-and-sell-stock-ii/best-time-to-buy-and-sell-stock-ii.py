class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        # for i in range(len(prices) - 1):
        #     if prices[i] < prices[i + 1]:
        #         res += prices[i + 1] - prices[i]
        
        # return res
        for buy, sell in zip(prices[:-1], prices[1:]):
            res += max(0, sell - buy)
        return res
