class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = the maximum profit
        # lowest = the lowest price that we've seen so far
        # iterate the day in prices
        # if I encounter a number > lowest, update res if (number - lowest) > res
        # if I encounter a number < lowest, update lowest = number
        # return res once reaches all numbers
        # time: O(n)  
        # space: O(1)

        res = 0
        lowest = prices[0]
        for p in prices:
            if p >= lowest:
                res = max(res, p - lowest)
            else:
                lowest = p
        
        return res