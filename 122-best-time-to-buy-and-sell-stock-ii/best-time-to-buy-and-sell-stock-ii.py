class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            if i > 0 and prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res