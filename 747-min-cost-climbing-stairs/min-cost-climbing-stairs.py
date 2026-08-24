class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # curr_cost -> cost1 -> cost2 -> top
        cost1, cost2 = cost[-1], 0
        for i in range(len(cost) - 2, -1, -1):
            curr_cost = cost[i] + min(cost1, cost2)
            cost2 = cost1
            cost1 = curr_cost
        return min(cost1, cost2)