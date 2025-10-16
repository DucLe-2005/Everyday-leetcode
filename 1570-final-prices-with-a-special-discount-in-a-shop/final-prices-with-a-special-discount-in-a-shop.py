class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = prices[:]

        for i, n in enumerate(prices):
            while stack and n <= prices[stack[-1]]:
                res[stack.pop()] -= n
            stack.append(i)
        
        return res
