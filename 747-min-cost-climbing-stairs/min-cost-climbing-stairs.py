class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # new_cost -> cost1 -> cost2
        cost1 = cost[-1]
        cost2 = 0
        for i in range(len(cost) - 2, -1, -1):
            new_cost = cost[i] + min(cost1, cost2)
            cost2 = cost1
            cost1 = new_cost
        
        return min(cost1, cost2)