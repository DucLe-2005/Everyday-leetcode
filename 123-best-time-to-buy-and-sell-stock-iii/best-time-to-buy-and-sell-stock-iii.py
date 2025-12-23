class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1: bidrectional dynamic programming
        # if len(prices) <= 1:
        #     return 0
        
        # left_min = prices[0]
        # right_max = prices[-1]
        # length = len(prices)
        # left_profits = [0] * length
        # right_profits = [0] * (length + 1)  # Allow to compare the result of having only one transaction

        # for l in range(1, length):
        #     left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
        #     left_min = min(left_min, prices[l])

        #     r = length - l - 1
        #     right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
        #     right_max = max(right_max, prices[r])

        # max_profit = 0
        # for i in range(0, length):
        #     max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])
        
        # return max_profit

        # Solution 2: One-Pass simmulation
        t1_cost, t2_cost = float("inf"), float("inf")
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # Profit after one transaction
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)

            # Reinvest the gaiuned profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)
        
        return t2_profit
        